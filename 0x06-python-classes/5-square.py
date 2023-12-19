#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor."""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""
        for x in range(self.size):
            for y in range(self.size):
                print("#", end="\n" if y is self.size - 1 and x != y else "")
        print()
