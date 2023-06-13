#!/usr/bin/python3
"""A module with a Square class"""


class Square:
    """A class that defines a square of a given size at a given position"""
    def __init__(self, size=0, position=(0, 0)):
        """Defines a square by size (private instance attribute)"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter def size(self, value): to set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Property def position(self): to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter def position(self, value): to set it"""
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")

            for row in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
