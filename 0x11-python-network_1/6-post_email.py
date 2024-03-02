#!/usr/bin/python3
import requests
import sys


def post_request(url, email):
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        response.raise_for_status()

        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    post_request(url, email)
