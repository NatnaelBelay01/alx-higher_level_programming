#!/usr/bin/python3

"""Defines a square class"""


class Square:
    def __init__(self, size=0):
        """Initializes the attributes.
        Args:
            size(int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """retrives the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """computes the area"""
        return (self.__size) ** 2
