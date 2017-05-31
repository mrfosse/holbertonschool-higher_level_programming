#!/usr/bin/python3
""" Returns true if the object is the same instance or inherited"""


def is_kind_of_class(obj, a_class):
    """Returns true if same instance or inherited, otherwise false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
