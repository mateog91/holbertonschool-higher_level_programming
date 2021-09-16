#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_value = 0
    for key in a_dictionary:
        current_value = a_dictionary[key]
        if current_value > best_value:
            best_key = key
            best_value = current_value
    return best_key
