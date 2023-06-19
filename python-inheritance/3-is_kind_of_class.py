#!/usr/bin/python3
"""A function which verifies whether the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance; otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
