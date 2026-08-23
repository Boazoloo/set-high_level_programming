#!/bin/bash
# A script that DELETE request passed as 1st argument and displays body of the reponse
curl -sX DELETE "$1"
