#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("\t- Body response:")
        print(f"\t\t- type: {type(body)}")
        print(f"\t\t- content: {body}")

except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
