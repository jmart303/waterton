import botocore.exceptions
from aws_inventory.microservices.client_services import get_aws_service_client
from aws_inventory.microservices.iam import credentials


class GetEc2:
	def __init__(self, account_list, region_list, logger):
		self.account_list = account_list
		self.region_list = region_list
		self.logger = logger

	def describe_ec2(self, account):
		print(f'searching {account}')
		instance_list = []
		audit_credentials = credentials.security_audit(account)
		for region in self.region_list:
			client = get_aws_service_client.get_client(region, 'ec2', audit_credentials)
			try:
				next_token_check = True
				instance_describe_run = 0
				next_token = None
				while next_token_check:
					if instance_describe_run == 0:
						ec2_response = client.describe_instances()
						for ec2_reservation in ec2_response["Reservations"]:
							for instances in ec2_reservation['Instances']:
								instance = instances['InstanceId']
								instance_list.append(instance)
								self.logger.info(f'{account} {region} {instance}')
								print(f'{region} {account} {instance}')
						instance_describe_run += 1
					else:
						if next_token is not None:
							ec2_response = client.describe_instances(NextToken=next_token)
							for ec2_reservation in ec2_response["Reservations"]:
								for instances in ec2_reservation['Instances']:
									instance = instances['InstanceId']
									self.logger.info(f'{account} {region} {instance}')
						else:
							next_token_check = False
			except botocore.exceptions.ClientError as error:
				self.logger.critical(f'error describing instance {error}')
			except botocore.exceptions.ParamValidationError as error:
				self.logger.critical(f'incorrect parameters {error}')
				