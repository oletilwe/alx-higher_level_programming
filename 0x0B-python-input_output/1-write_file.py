#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            characters_written = file.write(text)
            return characters_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
