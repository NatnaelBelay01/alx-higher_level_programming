#!/usr/bin/python3
"""A function that saves json representation to a file"""
import json


def save_to_json_file(my_obj, filename):
    """defines the dunction"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
