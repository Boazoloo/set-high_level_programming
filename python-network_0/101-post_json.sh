#!/bin/bash
# Send a JSON POST request and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
