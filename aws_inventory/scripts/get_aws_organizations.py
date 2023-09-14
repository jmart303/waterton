import os
from aws_inventory.microservices.organizations import get_aws_organizations
from aws_inventory.microservices.iam import credentials
from aws_inventory.microservices.client_services import get_aws_service_client

master_account = os.environ["aws_account"]

audit_credentials = credentials.security_audit(master_account)
client = get_aws_service_client.get_client('us-east-1', 'organizations', audit_credentials)

master_root_id = get_aws_organizations.GetRoots(client)
r_id = master_root_id.get_org_roots()
organizations = get_aws_organizations.ListOrganizations(client, r_id)
organization = organizations.list_org()

print(organization)
