import os
from aws_inventory.microservices.environment import get_aws_accounts
from aws_inventory.microservices.iam import credentials
from aws_inventory.microservices.client_services import get_aws_service_client

master_account = os.environ["aws_account"]
audit_credentials = credentials.security_audit(master_account)
client = get_aws_service_client.get_client('us-east-1', 'organizations', audit_credentials)
accounts = get_aws_accounts.GetAwsAccounts(client)
account = accounts.list_accounts()
for acct in account:
	print(acct)

