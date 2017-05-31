#!/usr/bin/python3
""" Empty class named baseGeometry"""


class BaseGeometry:
    """ Doesn't do anything yet but raise an exception """
    def area(self):
        """does nothing yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks to make sure value is an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
