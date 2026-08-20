#!/bin/bash
# Sends an OPTIONS request to the provided URL and displays all allowed HTTP methods
curl -sI "$1" | grep -i "^Allow:" | cut -d ' ' -f 2-
