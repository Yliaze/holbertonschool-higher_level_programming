#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle : Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Rectangle
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def widht(self):
        return self.__width

    @widht.setter
    def widht(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @widht.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @height.setter
    def y(self, value):
        self.__y = value
