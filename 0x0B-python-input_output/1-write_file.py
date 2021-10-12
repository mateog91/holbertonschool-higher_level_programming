#!/usr/bin/python3
"""Module for Task 1
 writes a string to a text file
 returns the number of characters written"""


def write_file(filename="", text=""):
    """returns the number of characters written:"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
