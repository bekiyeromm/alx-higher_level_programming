#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    if response.status_code == 200:
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    else:
        print("Error fetching {}: {}".format(url, response.status_code))
