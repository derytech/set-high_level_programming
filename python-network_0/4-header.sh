#!/bin/bash
# Sends a GET request to a URL with custom header X-School-User-Id: 98 and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
