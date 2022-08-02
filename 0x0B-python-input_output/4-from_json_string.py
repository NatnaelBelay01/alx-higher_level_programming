#!/usr/bin/python3
"""A function returning an object"""
import json


def from_json_string(my_str):
    """defines the function"""
    return json.loads(my_str)
