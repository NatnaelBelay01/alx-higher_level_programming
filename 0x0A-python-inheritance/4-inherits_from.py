#!/usr/bin/python3
"""A function to check inheretance"""


def inherits_from(obj, a_class):
    """ defines the function """
    st1, st2 = set(dir(obj)), set(dir(a_class))
    return st1 | st2 == st1 and st1 != st2
