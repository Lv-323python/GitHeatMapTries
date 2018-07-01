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
        custom_headers = {}
        if self.api_token:
            custom_headers = {'Authorization': 'token %s' % self.api_token}
        response = self.requests.get(url, custom_headers)
        return response.json()

    def get_repos(self, repo):
        """
        Gets github api repos
        :param repo: str
        :return: dict
        """
        endpoint = '/repos/%s/%s' % (self.owner, repo)
        return self._call(endpoint)

    def get_issues(self, repo):
        """
        Gets github api issues
        :param repo: str
        :return: dict
        """
        endpoint = '/repos/%s/%s/issues' % (self.owner, repo)
        return self._call(endpoint)

    def get_commits(self, repo):
        """
        Gets github api commits
        :param repo: str
        :return:  dict
        """
        endpoint = '/repos/%s/%s/git/commits' % (self.owner, repo)
        return self._call(endpoint)
