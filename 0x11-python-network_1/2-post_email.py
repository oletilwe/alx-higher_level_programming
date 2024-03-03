#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    content = response.read().decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
