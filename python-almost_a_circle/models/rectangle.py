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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def widht(self):
        """Getter for width"""
        return self.__width

    @widht.setter
    def widht(self, value):
        """Setter for width"""
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for heigth"""
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @widht.setter
    def x(self, value):
        """Setter for x"""
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @height.setter
    def y(self, value):
        """Setter for y"""
        self.__y = value
