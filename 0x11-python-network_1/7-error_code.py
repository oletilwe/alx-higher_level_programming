#!/usr/bin/python3
import requests
import sys


def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)
