#!/usr/bin/python3
def search_replace(my_list, search, replace):
    l = len(my_list)
    new = my_list[:]
    for index in range(l):
        if new[index] == search:
            new.pop(new[index])
            new.insert(index, replace)
    return (new)
