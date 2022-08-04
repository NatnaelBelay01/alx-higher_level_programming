#!/usr/python3
"""A base object"""


class Base():
    """defines the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the values"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
