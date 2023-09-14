import boto3


def security_audit(account):
	sts_client = boto3.client('sts')
	assumed_role_object = sts_client.assume_role(
		RoleArn='arn:aws:iam::' + account + ':role/SecurityAudit',
		RoleSessionName='AssumeRoleSecurityAuditSession',
		DurationSeconds=3600
	)
	credentials = assumed_role_object['Credentials']
	return credentials
