#!/bin/bash
# Send the required request to catch the server
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
