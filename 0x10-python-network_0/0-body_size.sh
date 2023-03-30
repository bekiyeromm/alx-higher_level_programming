#!bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo "$(curl -s -w "%{size_download}" $1)"
