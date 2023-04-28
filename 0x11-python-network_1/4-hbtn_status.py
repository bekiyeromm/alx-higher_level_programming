#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    if resp.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(resp.text)))
        print("\t- content: {}".format(resp.text))
    else:
        print("Error fetching {}: {}".format(url, resp.status_code))
