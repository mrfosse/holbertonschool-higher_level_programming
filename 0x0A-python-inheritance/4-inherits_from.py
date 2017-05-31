#!/usr/bin/python3
""" Returns true if the object is inherited"""


def inherits_from(obj, a_class):
    """Returns true if inherited, otherwise false"""
    if type(obj) is not a_class:
        if issubclass(type(obj), a_class):
            return True

    return False
