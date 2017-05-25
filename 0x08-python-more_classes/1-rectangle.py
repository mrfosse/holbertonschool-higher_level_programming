#!/usr/bin/python3
""" My Rectangle class """


class Rectangle:

    def __init__(self, width=0, height=0):
        """ initialize the retangles width and height """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Property and setter for width """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ propert and setter for height """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
