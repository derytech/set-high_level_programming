#!/bin/bash
# Sends a POST request to a URL with email and subject variables, displaying the response body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
