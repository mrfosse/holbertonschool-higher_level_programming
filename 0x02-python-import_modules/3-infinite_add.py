#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    i = 1
    total = 0;
    while i <= num:
        total = total + int(sys.argv[i])
        i = i + 1
    print("{:d}".format(total))
