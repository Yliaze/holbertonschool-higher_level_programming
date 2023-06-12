#!/usr/bin/python3
"""class Square"""


class Square:
    """Defines a square by size (private instance attribute)"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Property def size(self): to retrieve it"""
    @property
    def size(self):
        return self.__size

    """Property setter def size(self, value): to set it"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Property def position(self): to retrieve it"""
    @property
    def position(self):
        return self.__position

    """Property setter def position(self, value): to set it"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Returns the current square area"""
    def area(self):
        return self.__size * self.__size

    """Prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for row in range(self.__size):
            print(" " * self.__position[0], end="")
            for column in range(self.__size):
                print("#", end="")
            print()
