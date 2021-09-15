#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return [e1 for e1 in set_1 for e2 in set_2 if e1 != e2]
