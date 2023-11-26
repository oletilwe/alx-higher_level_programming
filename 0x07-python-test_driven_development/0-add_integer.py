#!/usr/bin/python3
#0_add_integer.py
"""Defines an integer addition function"""
def add_integer(a, b=98):
    """Return the integer addition of a and b.
    float arguments are typecasted to ints before addition is performed.
    TypeError : if either of a or b is a non-integer and non-float"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be integers or float")
    a = int(a)
    b = int(b)
    result = a + b
    return result
