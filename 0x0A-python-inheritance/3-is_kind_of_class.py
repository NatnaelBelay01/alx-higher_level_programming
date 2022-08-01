#!/usr/bin/python3
"""A function to check the type"""


def is_kind_of_class(obj, a_class):
    """Defines the function"""
    return(set(dir(obj)) | set(dir(a_class)) == set(dir(obj)))
