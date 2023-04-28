#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable found
in the header of the response.
"""


import urllib.request
import sys

address = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(address) as resp:
        x_request_id = resp.info()
        """print(resp.info()), from  out put of this you can grep value
        of X-Request-Id"""
        print(x_request_id['X-Request-Id'])
