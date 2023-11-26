#!/usr/bin/python3
# 4-print_square.py

"""a function that prints a square  with the character #"""


def print_square(size):
    """Check if size is an integer. Check if size is non-negative
    Check if size is a float and is less than 0. Print the square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
