#!/usr/bin/python3
# 5-text_indentation.py

"""A function that prints a text with 2 new lines"""


def text_indentation(text):
    """checks if the text is a string. checks if 2 new
    lines and checks the characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [',', '?', ':']
    current_line = ""

    for char in text:
        current_line += char

        if char in punctuation_marks:
            print(current_line.strip())
            print()
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
