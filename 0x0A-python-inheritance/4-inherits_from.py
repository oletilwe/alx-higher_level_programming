#!/usr/bin/python3
""" function that returns True if"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class
