#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a Square class"""

    def __init__(self, size=0):
        """Initializes attributes.
        Args:
            size(int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
