#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    true_counter = 0
    while i < x:
        try:
            value = my_list[i]
            print("{:d}".format(value), end="")
            i += 1
            true_counter += 1

        # except IndexError:
        #     break
        except (ValueError, TypeError):
            i += 1
            continue

    print("")
    return true_counter
