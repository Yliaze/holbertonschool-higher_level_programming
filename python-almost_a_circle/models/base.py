#!/usr/bin/python3
"""Base class"""


class Base:
    """Class Base : The "base” of all other classes

    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
