#!/usr/bin/python3
"""A fucntion that reads a file and prints it to the stdout"""


def read_file(filename=""):
    """Defines the function"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
