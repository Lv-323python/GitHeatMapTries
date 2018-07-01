
"""
Tests github api helper
"""

import os
from github_api_calls import Client


TOKEN = os.getenv("GITHUB_TOKEN")
USER = os.getenv("GITHUB_USER")
GITHUB_ORG = "Lv-323python"
CLIENT = Client(api_user=USER, api_token=TOKEN, org=GITHUB_ORG)

print(CLIENT.get_repos("learnRepo"))

