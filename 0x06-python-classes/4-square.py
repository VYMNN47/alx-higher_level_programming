#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Constructor."""
        self.size = size
    @property
    def size(self):
        """length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square"""
        return self.__size ** 2
