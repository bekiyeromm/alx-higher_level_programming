#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays thevalue of the X-Request-Id variable
"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        for header in response.info()._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
