#!/usr/bin/python3
"""Module for task 13 Advadced"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each
        line containing a specific string (see example):"""

    with open(filename, mode="r") as f:
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string
    # overrinding mode
    with open(filename, mode="w", encoding="utf-8") as s:
        s.write(new_content)
