#!/usr/bin/python3
"""A function that parses a string"""


def text_indentation(text):
    """parses a sting.
    Args:
        text(str): the sting to be parsed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i in ('.', '?', ':'):
            print('\n')
