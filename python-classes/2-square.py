#!/usr/bin/python3
"""class Square"""


class Square:
    """Defines a square by size (private instance attribute)"""
    def __init__(self, size=0):
        # isinstance(object, type)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
