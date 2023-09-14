import os
from datetime import datetime
from aws_inventory.microservices.client_services import get_aws_service_client
from aws_inventory.microservices.iam import credentials
from aws_inventory.microservices.environment import get_aws_accounts, get_aws_regions, setup_logging
from aws_inventory.microservices.ec2 import get_ec2_resources
import multiprocessing


def pull_instances(account_list, audit_credentials):
	procs = multiprocessing.cpu_count()

	get_regions = get_aws_regions.GetAwsRegions(master_account, audit_credentials)
	region_list = get_regions.get_regions()

	job_arguments = [
		[account]
		for account in account_list
	]
	try:
		with multiprocessing.Pool(processes=procs) as pool:
			ec2_query = get_ec2_resources.GetEc2(account_list, region_list, logger)
			pool.starmap(ec2_query.describe_ec2, job_arguments)
	except multiprocessing.ProcessError as e:
		mp_err = f'multiprocessing error occurred {e}'
		logger.critical(mp_err)
	
	
def pull_aws_accounts():
	audit_credentials = credentials.security_audit(master_account)
	org_client = get_aws_service_client.get_client('us-east-1', 'organizations', audit_credentials)
	get_aws_service_client.get_client('us-east-1', 'ec2', audit_credentials)
	get_accounts = get_aws_accounts.GetAwsAccounts(org_client)
	account_list = get_accounts.list_accounts()
	return account_list, audit_credentials


if __name__ == '__main__':
	start = datetime.now()
	log_date = start.strftime("%Y_%m_%d_%H_%M_%S")
	get_logger = setup_logging.Logger(start, f'../logs/aws_e2c_{log_date}.log')
	logger = get_logger.conf_logger()
	master_account = os.environ["aws_account"]
	try:
		accounts, credentials = pull_aws_accounts()
		pull_instances(accounts, credentials)
	except Exception as error:
		exception_error = f'main error occurred {error}'
		logger.critical(exception_error)
		