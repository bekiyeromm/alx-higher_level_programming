#!/bin/bash
# takes in a URL, ,sends a GET request to the URL, and displays the body of the respons having status code of 200
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
