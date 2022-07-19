#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """a class representaion of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the class.
        Args:
            size(int): the size of the square
            position(tuple): the position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrives the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrives the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if len(value) != 2 or type(value[0] or value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """computes the area"""
        return (self.__size) ** 2

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
