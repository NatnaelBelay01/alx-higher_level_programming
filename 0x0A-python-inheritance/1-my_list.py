#!/usr/bin/python3
"""a class the inherits from list"""


class MyList(list):
    """Defines the sub class"""

    def print_sorted(self):
        """a method that sorts the list"""
        print(sorted(self))
