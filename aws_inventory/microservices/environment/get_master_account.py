import boto3
import botocore.exceptions
import requests
import json


def pull_account():
	secret_name = "master_account"
	region_name = "us-east-1"
	session = boto3.session.Session()
	client = session.client(
		service_name='secretsmanager',
		region_name=region_name
	)
	try:
		response = client.get_secret_value(
			SecretId=secret_name
		)
	except requests.exceptions.ConnectionError as error:
		secret_manager_error = f'unable to contact secrets manager {error}'
		return 'Failed', secret_manager_error
	except botocore.exceptions.ParamValidationError as error:
		secret_manager_error = f'missing parameter {error}'
		return 'Failed', secret_manager_error
	else:
		secret = response['SecretString']
		formatSecret = json.loads(secret)
		account = formatSecret['account']
		return 'Success', account
	