#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    t = 0
    for l in range(0, x):
        try:
            print("{:d}".format(my_list[l]), end="")
            t += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (t)
