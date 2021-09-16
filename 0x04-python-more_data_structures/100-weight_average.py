#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0

    dotProduct = 0
    totalWeight = 0
    for element in my_list:
        dotProduct = dotProduct + (element[0] * element[1])
        totalWeight = totalWeight + element[1]

    return dotProduct / totalWeight
