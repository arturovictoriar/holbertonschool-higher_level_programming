#!/usr/bin/python3
"""
    rectangle.py module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Iniciatation method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    def display(self):
        """ Return the rectangle with the character #"""
        s = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                s += ("#" * self.__width)
                if i != self.__height - 1:
                    s += '\n'
        print(s)

    def area(self):
        """Return the rectangle's Area"""
        return self.__width * self.__height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x setter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
