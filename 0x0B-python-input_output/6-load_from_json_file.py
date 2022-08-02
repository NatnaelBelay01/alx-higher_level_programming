#!/usr/bin/python3
"""A function that returns an object from a jason file"""
import json


def load_from_json_file(filename):
    """defines the function"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
