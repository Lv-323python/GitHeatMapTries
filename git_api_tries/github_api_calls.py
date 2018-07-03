"""
This helper is for github api.
"""
import requests

BASE_API_GITHUB_URL = 'https://api.github.com'


class Client:
    """
    Realizes github api helper
    """

    def __init__(self, api_user, api_token=None, org=None):
        """
        Initializes client instance
        :param api_user: str
        :param api_token: str
        :param org: str
        """
        self.api_user = api_user
        self.api_token = api_token
        self.org = org
        self.owner = self.api_user if not self.org else self.org
        self.requests = requests
        self.base_url = BASE_API_GITHUB_URL

        self.requests_params = {
            'timeout': None,
            'proxies': None,
            'cert': None,
            'verify': None,
        }

    def _call(self, endpoint=""):
        """
        Gets github api data
        :param endpoint: str
        :param authorized: bool
        :return: dict
        """
        url = self.base_url + endpoint
        custom_headers = ()
        if self.api_token:
            custom_headers = (self.api_user, self.api_token)
        response = requests.get(url, auth=custom_headers)
        return response.json()

    def get_repo(self, repo):
        """
        Gets github api repo of user or org by name
        :param repo: str
        :return: dict
        """
        endpoint = '/repos/{owner}/{repo}'.format(owner=self.owner, repo=repo)
        return self._call(endpoint)

    def get_issues(self, repo):
        """
        Gets github api issues
        :param repo: str
        :return: dict
        """
        endpoint = '/repos/{owner}/{repo}/issues'.format(owner=self.owner, repo=repo)
        return self._call(endpoint)

    def get_commits(self, repo):
        """
        Gets github api commits
        :param repo: str
        :return:  dict
        """
        endpoint = '/repos/{owner}/{repo}/commits'.format(owner=self.owner, repo=repo)
        return self._call(endpoint)

    def get_contributors_from_repo(self, repo):
        """
        Gets github api commits
        :param repo: str
        :return:  dict
        """
        endpoint = '/repos/{owner}/{repo}/contributors'.format(owner=self.owner, repo=repo)
        return self._call(endpoint)

    def get_user_commits_from_repo(self, repo, user):
        """
        Gets github api commits
        :param repo: str
        :return:  dict
        :user: str
        """
        endpoint = '/repos/{owner}/{repo}/commits'.format(owner=self.owner, repo=repo)
        list_of_commits = self._call(endpoint)
        list_user_commits = []
        for commit in list_of_commits:
            if commit['commit']['author']['name'] == user:
                list_user_commits.append(commit['commit'])
        return list_user_commits

    def get_org_members(self):
        """
        Gets github api commits
        :param repo: str
        :return:  dict
        :user: str
        """
        endpoint = '/orgs/{owner}/members'.format(owner=self.owner)
        return self._call(endpoint)

    def get_user(self):
        """
        Gets github api commits
        :param repo: str
        :return:  dict
        :user: str
        """
        endpoint = '/user'
        return self._call(endpoint)
