#!/usr/bin/python3
"""A function to check an instance's presence"""


def is_same_class(obj, a_class):
    """defines the function"""
    if type(obj) is a_class:
        return True
    return False
