#!/usr/bin/python3
a = 0
b = 1
while a <= 9:
    c = b
    while c <= 9:
        if a == 8 and c == 9:
            print("{}{}".format(a, c))
        else:
            print("{}{}, ".format(a, c), end="")
        c = c + 1
    a = a + 1
    b = b + 1
