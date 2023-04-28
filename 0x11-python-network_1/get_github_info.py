#!/usr/bin/env python3
"""Python script that uses the requests and sys packages to fetch information
about a GitHub repository, based on the given repository name and
owner name
"""


import requests
import sys

def get_repo_info(repo_name, owner_name):
    # Construct the GitHub API URL for the repository
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    
    # Send a GET request to the API and get the response
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the repository information from the response JSON
        repo_info = response.json()
        
        # Print the repository information
        print(f"Repository Name: {repo_info['name']}")
        print(f"Description: {repo_info['description']}")
        print(f"Language: {repo_info['language']}")
        print(f"Forks: {repo_info['forks']}")
        print(f"Stars: {repo_info['stargazers_count']}")
    else:
        # Print an error message if the request failed
        print(f"Error: {response.status_code} - {response.reason}")
        
if __name__ == "__main__":
    # Get the repository and owner names from the command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    # Call the get_repo_info function with the given arguments
    get_repo_info(repo_name, owner_name)
