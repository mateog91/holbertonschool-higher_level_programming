#!/bin/python3
"""This module has only one function ''text_indentation''
Description:
- text must be a string, otherwise raise a TypeError exception with the
  message text must be a string
- There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """returns nothing 

    Args:
        text (str): string to be indented.

    Description:
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    delim = ".?:"
    flag = True
    for current_char in text:
        if current_char == " " and flag == True:
            continue
        elif flag == True:
            flag = False
        if current_char not in delim and flag == False:
            print(current_char, end="")
            continue
        elif flag == False:
            print("{:s}\n".format(current_char))
            flag = True
