#!/usr/bin/python3
"""A function that appends"""


def append_write(filename="", text=""):
    """defines the function"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
