#!/usr/bin/python3
""" """


import requests
import sys

if __name__ == "__main__":
    # Get the username and password from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Set up the API endpoint URL
    url = 'https://api.github.com/user'

    # Send a GET request to the endpoint using Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Extract the id from the response JSON data
        user_id = response.json()['id']
        print(f"{user_id}")
    else:
        # If the response was not successful, print the status code and message
        print(f"{None}")
