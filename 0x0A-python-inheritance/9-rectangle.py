#!/usr/bin/python3
""" starting our rectangle class using basegeometry as a parent"""


class BaseGeometry:
    """ Parent class of Rectangles and soon to be squares """
    def area(self):
        """does nothing yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks to make sure value is an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """inits rectangle with width and height"""
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates the area of a Recatangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(type(
                self).__name__, self.__width, self.__height)
