#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Representation of a square class"""
    def __init__(self, size=0):
        """initializes the size:
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
        """Retrives the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the new value of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area"""
        return (self.__size) ** 2

    def my_print(self):
        """prints a square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
