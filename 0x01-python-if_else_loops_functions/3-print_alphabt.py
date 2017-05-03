#!/usr/bin/python3
i = 0
while i < 26:
    l = ord('a') + i
    if chr(l) != 'q' and chr(l) != 'e':
        print("{}".format(chr(l)), end="")
    i = i + 1
