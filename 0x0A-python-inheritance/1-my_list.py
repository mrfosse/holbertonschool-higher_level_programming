#!/usr/bin/python3
""" inherits from list and prints in ascending order"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        pass

    def print_sorted(self):
        """Prints in ascending order"""
        print(sorted(self))
