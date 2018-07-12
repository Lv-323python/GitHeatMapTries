
"""
Tests github api helper
"""

import os
from git_api_tries import github_api_calls
import json


#TOKEN = os.getenv("GITHUB_TOKEN")
TOKEN='38bdfcb675dc130b977824f008b4379753ab34f8'
#USER = os.getenv("GITHUB_USER")
USER='Anastasiia-Khab'
GITHUB_ORG = "Lv-323python"
CLIENT = github_api_calls.Client(api_user=USER, api_token=TOKEN, org=GITHUB_ORG)
CLIENT2 = github_api_calls.Client(api_user=USER, api_token=TOKEN)

#print(CLIENT.get_repos("learnRepo"))'
print('\n____________________________________\n')
print(CLIENT2.get_user())
#print(CLIENT.get_org_members())
#print(CLIENT.owner)
#print(CLIENT2.owner)
#print(CLIENT.get_repo('learnRepo')['created_at'])

#print(type(CLIENT.get_repo('learnRepo')))
#print(type(CLIENT.get_repo('learnRepo')['id']))

#print(type(CLIENT.get_commits('learnRepo')))
#print(CLIENT.get_commits('learnRepo'))

response=CLIENT.get_repo('learnRepo')
result=[]
result.append({'id':response['id'],
                         'reponame':response['name'],
                         'datecreated':response['created_at'],
                         'owner':response['owner']['login'],
                         'url':response['url']})
print(json.dumps(result))

print('/n____________________________________________________/n')
import requests
response=requests.get('https://api.github.com/repos/Lv-323python/learnRepo/commits').json()
result=[]
for commit in response:
    result.append({'hash': commit['sha'],
                   'author': commit['commit']['author']['name'],
                   'message': commit['commit']['message'],
                   'date': 0})
print(result)

#print(json.dumps(response))





