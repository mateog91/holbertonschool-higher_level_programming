#!/usr/bin/python3
"""Module for task 13 Advadced"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each
        line containing a specific string (see example):"""
    # new = ""
    # with open(filename, mode="r", encoding="utf-8") as myFile:
    #     for line in myFile:
    #         new += line
    #         print(new)
    #         if search_string in line:
    #             new += new_string

    #     # myFile.write(new)

    new = ""
    # Opening file
    with open(filename, mode="r") as myFile:
        for line in myFile:
            new += line
            if search_string in line:
                new += new_string
    # overrinding mode
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        writeFile.write(new)
