#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        print()
        return (0)
    try:
        print("{:d}".format(value), end="")
        print()
        return True
    except:
        return(False)
