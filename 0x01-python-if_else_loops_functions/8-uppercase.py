#!/usr/bin/python3
def uppercase(str):
    for i in str:
        l = ord(i)
        if l > 96 and l < 123:
            l = l - 32
        print("{}".format(chr(l)), end="")
    print("")
