#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num < 1:
        print("{:d} argument.".format(num))
    elif num == 1:
        print("{:d} argument:".format(num))
    else:
        print("{:d} arguments:".format(num))
    if num > 0:
        i = 1
        while i <= num:
            print("{:d}: {}".format(i, sys.argv[i]))
            i = i + 1
