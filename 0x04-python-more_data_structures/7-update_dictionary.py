#!/usr/bin/python3
print_sorted_dictionary = __import__(
    '6-print_sorted_dictionary').print_sorted_dictionary


def update_dictionary(a_dictionary, key, value):
    d = {key: value}
    a_dictionary.update(d)
