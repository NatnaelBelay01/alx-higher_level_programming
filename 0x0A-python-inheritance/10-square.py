#!/usr/bin/python3
"""A square representation"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """initiates the variables"""
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
