#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
try:
    with urllib.request.urlopen(url) as response:
        if response.getcode() == 200:
            body = response.read().decode('utf-8')
            print('-' * 50)
            print(f"Body response:\n{body}")
            print('-' * 50)

            headers = response.info()
            print("HTTP Headers:")
            for header, value in headers.items():
                print(f"{header}: {value}")

        else:
            print(f"Error code: {response.getcode()}")

except urllib.error.HTTPError as e:
    print(f"HTTPError: {e}")
except urllib.error.URLError as e:
    print(f"URLError: {e}")
