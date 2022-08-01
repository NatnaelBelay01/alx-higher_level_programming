#!/usr/bin/python3
"""A function to check inheretance"""


def inherits_from(obj, a_class):
    """ defines the function """
    return issubclass(type(obj), a_class) and type(obj) != a_class
