import boto3


def get_client(region, service, credentials):
	client = boto3.client(
		service,
		region_name=region,
		aws_access_key_id=credentials['AccessKeyId'],
		aws_secret_access_key=credentials['SecretAccessKey'],
		aws_session_token=credentials['SessionToken']
	)
	return client


def get_resource(region, service, credentials):
	resource = boto3.resource(
		service,
		region_name=region,
		aws_access_key_id=credentials['AccessKeyId'],
		aws_secret_access_key=credentials['SecretAccessKey'],
		aws_session_token=credentials['SessionToken']
	)
	return resource

