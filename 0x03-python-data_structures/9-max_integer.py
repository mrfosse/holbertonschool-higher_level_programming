#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (None)
    l = len(my_list) - 1
    i = 0
    top = my_list[i]
    while i <= l:
        if my_list[i] > top:
            top = my_list[i]
        i = i + 1
    return (top)
