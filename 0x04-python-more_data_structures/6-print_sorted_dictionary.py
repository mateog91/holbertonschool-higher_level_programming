#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    slist = sorted(a_dictionary.keys())
    for element in slist:
        print("{:s}: {}".format(element, a_dictionary[element]))
