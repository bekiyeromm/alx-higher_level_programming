#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays thevalue of the X-Request-Id variable
found in the header of the response
"""


import urllib.request
import sys

reqst = urllib.request.Request(sys.argv[1])

if __name__ == "__main__":
    with urllib.request.urlopen(reqst) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
