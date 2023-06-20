#!/usr/bin/python3
"""
class BaseGeometry: Superclass

class Rectangel: Subclass

Args:
    width (int): width of the rectangle
    height (int): height of the rectangle
"""


class BaseGeometry():
    """Class BaseGeometry"""
    def area(self):
        """Raise an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle, subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation using BaseGeometry(superclass) function"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "heigth", height)
        self.__width = width
        self.__height = height
