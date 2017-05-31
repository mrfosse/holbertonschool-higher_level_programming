#!/usr/bin/python3
""" Returns true if the object is exactly the same instance"""


def is_same_class(obj, a_class):
    """Returns true if same instance, otherwise false"""
    if type(obj) is a_class:
        return True
    else:
        return False
