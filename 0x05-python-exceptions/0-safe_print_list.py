#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0 or my_list is None or my_list == []:
        print()
        return (0)
    try:
        for count in range(x):
            print("{}".format(my_list[count]), end="")
        print()
    except:
        print()
        return(count)
    return (count + 1)
