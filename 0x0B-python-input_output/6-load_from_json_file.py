#!/usr/bin/python3
"""Module for Task 5
    Write a function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”:"""
    with open(filename, mode="r", encoding="UTF-8") as myFile:
        return json.load(myFile)
