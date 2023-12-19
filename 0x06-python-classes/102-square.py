#!/usr/bin/python3
"""Square module"""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor"""

        self.size = size

    @property
    def size(self):
        """comment"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the size"""
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()
