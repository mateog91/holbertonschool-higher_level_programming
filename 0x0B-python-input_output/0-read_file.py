#!/usr/bin/python3
"""Module for Task 0"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())


read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
