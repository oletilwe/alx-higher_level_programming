#!/usr/bin/python3
# 3-say_my_name.py

"""Prints the full name based on the given first and last names."""


def say_my_name(first_name, last_name=""):
    """checks if both names are entered. checks if both names are
    strings and prints them"""
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
