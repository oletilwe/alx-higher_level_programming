#!/usr/bin/python3
import requests
import sys


def get_github_user_id(username, access_token):
    try:
        url = "https://api.github.com/user"
        auth = (username, access_token)
        response = requests.get(url, auth=auth)
        response.raise_for_status()

        user_id = response.json().get('id')
        print(f"Your GitHub user id is: {user_id}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    get_github_user_id(username, access_token)
