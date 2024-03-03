#!/usr/bin/python3
import requests
import sys


if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

response = requests.post(url, data=data)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
