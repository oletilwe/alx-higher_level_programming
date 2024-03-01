#!/usr/bin/python3
import urllib.request

URL = 'https://alx-intranet.hbtn.io/status'
try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print('-' * 50)
        print(f"Body response:\n{body}")
        print('-' * 50)
except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
