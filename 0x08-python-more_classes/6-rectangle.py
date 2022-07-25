#!/usr/bin/python3

"""A class that represents a rectangel"""


class Rectangle:
    """a class representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the class.
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        j = {width: 'width', height: 'height'}
        for i in (width, height):
            if type(i) is not int:
                raise TypeError("{} must be an integer".format(j[i]))
            if i < 0:
                raise ValueError("{} must be >= 0".format(j[i]))
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """Returns a sting that can be converted to an obj"""
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @property
    def width(self):
        """Retrives the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A method that returns the area"""
        return (self.__width) * (self.__height)

    def perimeter(self):
        """A method that returns the perimeter"""
        return (2 * self.__width) + (2 * self.__height)

    def __del__(self):
        """deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
