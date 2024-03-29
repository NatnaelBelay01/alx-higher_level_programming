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
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
