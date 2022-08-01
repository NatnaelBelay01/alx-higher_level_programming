#!/usr/bin/python3
"""A class that inherits """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines the class"""

    def __init__(self, width, height):
        """initializes the variables
        Args:
            width (int): the width.
            height (int): the height.
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        nam = str(self.__class__.__name__)
        return "[{}] {}/{}".format(nam, self.__width, self.__height)
