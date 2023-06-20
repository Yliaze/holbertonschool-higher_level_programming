#!/usr/bin/python3
"""class Square: subclass that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Class Square, subclass of BaseGeometry

    Args:
        size (int): size of the square
    """
    def __init__(self, size):
        """Instantiation using BaseGeometry(superclass) function"""
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return description of the rectangle/square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
