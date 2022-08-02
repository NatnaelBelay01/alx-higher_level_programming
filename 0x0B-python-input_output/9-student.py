#!/usr/bin/python3
"""A class that defines a student obj"""


class Student():
    """defiens the class"""

    def __init__(self, first_name, last_name, age):
        """initializes the variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives dictionary representation of Student"""
        return self.__dict__
