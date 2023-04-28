#!/usr/bin/python3
"""a script that fetches https://alx-intranet.hbtn.io/status
must use the package urllib and must use a with statement
"""


import urllib.request

address = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(address) as resp:
        html = resp.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))
