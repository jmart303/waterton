
class GetRoots:
	def __init__(self, service):
		self.service = service
		
	def get_org_roots(self):
		listRoots = self.service.list_roots(
		)
		root_id = listRoots['Roots'][0]['Id']
		return root_id


class ListOrganizations:
	def __init__(self, service, r_id):
		self.service = service
		self.r_id = r_id
	
	def list_org(self):
		org_list = []
		response = self.service.list_organizational_units_for_parent(
			ParentId=self.r_id
		)
		for org in response['OrganizationalUnits']:
			org_list.append(org)
		return org_list
