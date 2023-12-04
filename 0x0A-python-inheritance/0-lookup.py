#!/usr/bin/python3
"""a list of attributes"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return [attr for attr in dir(obj) if not callable(
        getattr(obj, attr)) or hasattr(getattr(obj, attr), '__call__')
        ]
