#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
