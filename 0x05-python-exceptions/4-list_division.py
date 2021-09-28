#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0

    while i < list_length:
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            opp = a / b
            new_list.append(opp)

        except IndexError:
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
        finally:
            i += 1

    return new_list
