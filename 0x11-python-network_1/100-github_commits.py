#!/usr/bin/python3
""" """


import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    # Parse the response JSON data
    commits = res.json()
    for commit in commits[0:10:1]:
        commit_id = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{commit_id}: {author}")
