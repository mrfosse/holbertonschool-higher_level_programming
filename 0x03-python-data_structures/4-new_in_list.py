#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return(None)
    if idx >= len(my_list) or idx < 0:
        return(my_list)
    else:
        new = my_list[:]
        new[idx] = element
        return(new)
