#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id You must use Basic Authentication
with a personal access token as password first argument will be your username
second argument will be your personal access token as password
"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    """sys.argv[1] = repo owner and sys.argv[2] = owner[repo]"""
    basic_auth = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=basic_auth)
    print(req.json().get("id"))
