#!/usr/bin/python3
"""Module for Task 2
 appends a string to a text file
 returns the number of characters written"""


def append_write(filename="", text=""):
    """returns the number of characters written:"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
