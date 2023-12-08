#!/usr/bin/python3
"""Class Rectangle inherits from Base"""
from models.base import Base


def __init__(self, width, height, x=0, y=0, id=None):
    super().__init__(id)

    self.__width = width
    self.__height = height
    self.__x = x
    self.__y = y


def width(self):
    return self.__width


def width(self, value):
    self._validate_positive_integer("width", value)
    self.__width = value


def height(self):
    return self.__height


def height(self, value):
    self._validate_positive_integer("height", value)
    self.__height = value


def x(self):
    return self.__x


def x(self, value):
    self._validate_non_negative_integer("x", value)
    self.__x = value


def y(self):
    return self.__y


def y(self, value):
    self._validate_non_negative_integer("y", value)
    self.__y = value


def _validate_positive_integer(self, attribute_name, value):
    if not isinstance(value, int):
        raise TypeError(f"{attribute_name} must be an integer.")
    elif value <= 0:
        raise ValueError(f"{attribute_name} must be > 0.")

def _validate_non_negative_integer(self, attribute_name, value):
    if not isinstance(value, int):
        raise TypeError(f"{attribute_name} must be an integer.")
    elif value < 0:
        raise ValueError(f"{attribute_name} must be >= 0.")
