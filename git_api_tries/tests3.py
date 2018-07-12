
"""
Tests github api helper
"""

import os
import json
from request_sender.github_request_sender import GithubRequestSender



#TOKEN = os.getenv("GITHUB_TOKEN")
TOKEN=''
#USER = os.getenv("GITHUB_USER")
USER='Anastasiia-Khab'
GITHUB_ORG = "Lv-323python"

CLIENT = GithubRequestSender(base_url="https://api.github.com", repo='learnRepo', owner="Lv-323python")

#print(CLIENT.get_repos("learnRepo"))'
print('\n____________________________________\n')
print(CLIENT.owner)
print(CLIENT.get_repo())


print(type(CLIENT.get_commits()))
#print(CLIENT.get_commits())

print(CLIENT.get_commit_by_hash('ddc35f6a775b3c8e0b22b3df945d48cbe7369c32'))


#print(json.dumps(response))