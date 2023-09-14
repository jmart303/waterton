
class GetAwsAccounts:
	def __init__(self, service):
		self.service = service
	
	def list_accounts(self):
		account_list = []
		paginator = self.service.get_paginator('list_accounts')
		page_iterator = paginator.paginate()
		for page in page_iterator:
			for acct in page['Accounts']:
				iD = acct['Id']
				name = acct['Name']
				status = acct['Status']
				data = f'{status} {iD} {name}'
				account_list.append(iD)
				# account_list.append(data)
		return account_list
