#!/usr/bin/python3
import urllib.request
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(f"X-Request-Id value: {x_request_id}")

except urllib.error.URLError as e:
    print(f"Error: {e}")
