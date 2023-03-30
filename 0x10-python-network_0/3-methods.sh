#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -X -s -I OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
