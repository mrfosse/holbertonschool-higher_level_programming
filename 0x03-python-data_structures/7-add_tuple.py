#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = [0, 0]
    list2 = [0, 0]
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 > 2:
        len1 = 2
    if len2 > 2:
        len2 = 2
    for i in range(len1):
        list1[i] += tuple_a[i]
    for i in range(len2):
        list2[i] += tuple_b[i]
    total = (list1[0] + list2[0], list1[1] + list2[1])
    return (total)
