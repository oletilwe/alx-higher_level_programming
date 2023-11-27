#!/usr/bin/python3
"""defines a rectangle class along with its value"""


class Rectangle:
    """Represents the rectangle and its value"""
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    def height(self):
        """Get/set the height of the rectangle."""
        return self._height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def width(self):
        """Get/set the width of the rectangle."""
        return self._width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
