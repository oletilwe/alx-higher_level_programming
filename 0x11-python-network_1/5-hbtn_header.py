#!/usr/bin/python3
import requests
import sys


def get_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        request_id = response.headers.get("X-Request-Id")
        if request_id:
            print(f"{request_id}")
        else:
            print("X-Request-Id not found in the response headers.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_request_id(url)
