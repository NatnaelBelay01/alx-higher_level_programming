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
