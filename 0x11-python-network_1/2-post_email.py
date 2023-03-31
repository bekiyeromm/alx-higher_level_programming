#!/usr/bin/python3
"""script for testing POST requests so servers"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    payload = (urllib.parse.urlencode(payload)).encode('ascii')
    req = urllib.request.Request(url, payload)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
