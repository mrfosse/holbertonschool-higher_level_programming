#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for count in range(x):
        try:
            print("{:d}".format(my_list[count]), end="")
            i = i + 1
        except:
            continue
    print()
    return (i)
