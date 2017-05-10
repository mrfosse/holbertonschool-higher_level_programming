#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (None)
    l = len(my_list) - 1
    i = 0
    new = my_list[:]
    while i <= l:
        if my_list[i] % 2 == 0:
            new[i] = True
        else:
            new[i] = False
        i = i + 1
    return (new)
