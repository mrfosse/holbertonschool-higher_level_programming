#!/usr/bin/python3
i = 0
flag = 1
while i < 26:
    l = ord('z') - i
    if flag == -1:
        l = l - 32
    print("{}".format(chr(l)), end="")
    i = i + 1
    flag = flag * -1
