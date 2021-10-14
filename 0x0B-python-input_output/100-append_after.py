#!/usr/bin/python3
"""Module for task 13 Advadced"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each
        line containing a specific string (see example):"""

    with open(filename, mode="a", encoding="UTF-8") as myFile:
        new = ""
        for line in myFile.readlines():
            if search_string in line:
                new += line + new_string
            else:
                new += line

    # overrinding mode
    with open(filename, mode="w", encoding="utf-8") as s:
        s.write(new)
