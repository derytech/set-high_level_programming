#!/bin/bash
# Sends a JSON POST request with the contents of a file to a given URL
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
