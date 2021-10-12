#!/usr/bin/python3
"""Module for Task 3
    function that returns an object (Python data structure)
    represented by a JSON string:"""
import json


def from_json_string(my_str):
    """returns object (Python data structure)
    represented by a JSON string"""
    return json.load(my_str)
