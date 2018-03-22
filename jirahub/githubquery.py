# Licensed under a 3-clause BSD style license - see LICENSE.rst
# This module implements the GithubQuery class.

from github import Github

__all__=['GithubQuery']


class GithubQuery(object):
    """Class to query and update a github repository for comparing to JIRA
    """

    def __init__(self, repo, key=None, user=None, password=None):
        """Class to query and update a github repository for comparing to JIRA

        Parameters
        ----------
        repo: str
            Name of a repository to track and update the issues.  The name of the repository
            should be in the form of 'username/name'

        key: str
            Authentification token for the current user

        user: str
            Username for the current user

        password: str
            password for the current user
        """

        # authenticate with github
        if key:
           self.github = Github(key)
        elif user is not None:
           self.github = Githubh(user, password)
        else:
           self.github = Github()

        # link to the current rero
        user_name, repo_name = repo.split('/')
        self.repo = self.github.get_user(user_name).get_repo(repo_name)

