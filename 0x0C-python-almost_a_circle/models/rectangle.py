#!/usr/bin/python3
"""A class representation of a rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines the rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the values"""
        super().__init__(id)
        j = {width: 'width', height: 'height', x: 'x', y: 'y'}
        for i in (width, height, x, y):
            if type(i) is not int:
                raise TypeError("{} must be an integer".format(j[i]))
            if i < 0:
                raise ValueError("{} must be >= 0".format(j[i]))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the width"""
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
        """Retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Retrives the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrives the height"""
        return self.__y

    @height.setter
    def y(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area"""
        return self.__height * self.__width

    def display(self):
        """prints the area"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns a printable"""
        return "[Rectangle] ({:d}) {:d}/{:d}" \
                "- {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the values"""
        atrlst = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, j in enumerate(args):
                setattr(self, atrlst[i], j)
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)
