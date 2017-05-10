#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0 or len(my_list) < 1:
        return(None)
    else:
        my_list[idx] = element
        return(my_list)
