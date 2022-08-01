#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""A class BaseGeommetry"""


class Rectangle(BaseGeometry):
    """defines the class"""

    def __init__(self, width, height):
        """initializes the variables"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
