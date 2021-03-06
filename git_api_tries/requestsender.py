"""
Contains GithubRequestSender class that provides implementation of
interface for sending API requests
to web-based hosting services for version control using GitHub
"""

from datetime import datetime
import requests
from request_sender_base import RequestSender

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class GithubRequestSender(RequestSender):
    """
    Class that provides implementation of interface for sending API requests
    to web-based hosting services for version control using GitHub
    """

    def __init__(self, owner, repo, base_url="https://api.github.com"):
        RequestSender.__init__(self,
                               base_url=base_url,
                               owner=owner,
                               repo=repo)

    def get_repo(self):
        """
        Gets repository info in JSON format
        example:
        {
            "id": "unique id",
            "repo_name": "repository name",
            "creation_date": "date",
            "owner": "repository owner",
            "url": "repository url"
        }
        :return: string - JSON formatted response
        """

        endpoint = '/repos/{owner}/{repo}'.format(owner=self.owner, repo=self.repo)
        response = requests.get(self.base_url + endpoint).json()
        creation_date = datetime.strptime(response['created_at'], GITHUB_TIME_FORMAT).timestamp()
        repo = {'id': response['id'],
                'repo_name': response['name'],
                'creation_date': creation_date,
                'owner': response['owner']['login'],
                'url': response['url']}
        return repo

    def get_branches(self):
        """
        Gets information about branches in JSON format
        example:
        [
            {
                "name": "branch name"
            },
            ...
        ]
        :return: string - JSON formatted response
        """
        endpoint = '/repos/{owner}/{repo}/branches'.format(owner=self.owner, repo=self.repo)
        url = self.base_url + endpoint
        response = requests.get(url).json()
        branches = []
        for raw in response:
            if raw['name']:
                branches.append({'name': raw['name']})
        return branches

    def get_commits(self):
        """
        Gets information about commits in JSON format
        example:
        [
            {
                "hash": "commit hash",
                "author": "commit author",
                "message": "commit message",
                "date": "date when committed"
            },
            ...
        ]
        :return: string - JSON formatted response
        """
        endpoint = '/repos/{owner}/{repo}/commits'.format(owner=self.owner, repo=self.repo)
        response = list(requests.get(self.base_url + endpoint).json())
        commits = []
        for _, commit in enumerate(response):
            date = datetime.strptime(commit['commit']['author']['date'],
                                     GITHUB_TIME_FORMAT).timestamp()
            commits.append({'hash': commit['sha'],
                            'author': commit['commit']['author']['name'],
                            'message': commit['commit']['message'],
                            'date': date})

return commits