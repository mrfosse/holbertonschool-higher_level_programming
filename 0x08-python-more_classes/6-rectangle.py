#!/usr/bin/python3
""" My Rectangle class """


class Rectangle:

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initialize the retangles width and height """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def area(self):
        """ Define Area function """
        return self.__width * self.__height

    def perimeter(self):
        """ Define perimeter Function """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints the rectangle with '#' """
        string1 = ""
        string2 = ""
        if self.__width is not 0 and self.__height is not 0:
            for i in range(0, self.__width):
                string1 = string1 + '#'
            for j in range(0, self.__height):
                string2 = string2 + "\n" + string1
        return (string2)

    def __repr__(self):
        """ prints a copy of the rectangle. """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Garbage collector for rectangle """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
