#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is []:
        return my_list
    return [True if e % 2 == 0 else False for e in my_list]
