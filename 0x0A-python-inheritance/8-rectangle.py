#!/usr/bin/python3
"""A class BaseGeommetry"""

class BaseGeometry():
    """defines the class"""

    def area(self):
        """defines a method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """defines a method that validates values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""A class that inherits """


class Rectangle(BaseGeometry):
    """defines the class"""

    def __init__(self, width, height):
        """initializes the variables"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
