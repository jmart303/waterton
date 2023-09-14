import boto3


class GetAwsRegions:
	def __init__(self, account, credentials):
		self.master_account = account
		self.credentials = credentials
		
	def get_regions(self):
		enabled_regions = []
		sess = boto3.Session()
		acct_regions = sess.get_available_regions('ec2')
		for region in acct_regions:
			try:
				regional_sts = boto3.client(
					"sts",
					region_name=region,
					aws_access_key_id=self.credentials["AccessKeyId"],
					aws_secret_access_key=self.credentials["SecretAccessKey"],
					aws_session_token=self.credentials["SessionToken"],
				)
				regional_sts.get_caller_identity()
			except Exception as boto3_error:
				pass
			else:
				enabled_regions.append(region)
		return enabled_regions
