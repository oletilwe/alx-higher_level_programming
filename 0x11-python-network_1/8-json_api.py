#!/usr/bin/python3
import sys
import requests


def search_user(letter):
    try:
        url = "http://0.0.0.0:5000/search_user"
        data = {'q': letter}

        response = requests.post(url, data=data)
        response.raise_for_status()

        try:
            json_data = response.json()
            if json_data:
                user_id = json_data.get('id')
                user_name = json_data.get('name')
                print(f"[{user_id}] {user_name}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Check if an argument is provided, otherwise set q=""
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user(letter)
