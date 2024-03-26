#!/usr/bin/node
"""
Write a script that reads and prints the content of a file.
"""

import sys


def read_and_print_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the file path as the first argument.")
    else:
        file_path = sys.argv[1]
        read_and_print_file(file_path)
