#!/bin/bash
# Takes in a URL, sends a request using curl, and displays the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
