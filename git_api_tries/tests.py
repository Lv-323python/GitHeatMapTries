
"""
Tests github api helper
"""

import os
from git_api_tries import github_api_calls


#TOKEN = os.getenv("GITHUB_TOKEN")
TOKEN='1e50e30313ae5f77c366429776cb3a23453f4096'
#USER = os.getenv("GITHUB_USER")
USER='Anastasiia-Khab'
GITHUB_ORG = "Lv-323python"
CLIENT = github_api_calls.Client(api_user=USER, api_token=TOKEN, org=GITHUB_ORG)
CLIENT2 = github_api_calls.Client(api_user=USER, api_token=TOKEN)

#print(CLIENT.get_repos("learnRepo"))'
print('\n____________________________________\n')
print(CLIENT2.get_user())
print(CLIENT.get_org_members())
print(CLIENT.owner)
print(CLIENT2.owner)