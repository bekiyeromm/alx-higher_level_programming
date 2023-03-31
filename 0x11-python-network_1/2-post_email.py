#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8
"""
import urllib.parse
import urllib.request
import sys


url = sys.argv[1]
email = sys.argv[2].encode("utf-8")
data = urllib.parse.urlencode({'email': email})
data = data.encode('ascii')

if __name__ == "__main__":
    with urllib.request.urlopen(url, data) as response:
        resp = response.read()
        cont = resp.decode("utf-8")
        print(cont)
