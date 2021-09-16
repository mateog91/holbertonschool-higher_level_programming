#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mult(x, y): return x * y
    lst_number = [number] * len(my_list)
    return list(map(mult, my_list, lst_number))
