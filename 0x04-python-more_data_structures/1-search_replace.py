#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace = [element if element !=
               search else replace for element in my_list]
    return replace
