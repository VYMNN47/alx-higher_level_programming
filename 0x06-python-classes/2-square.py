#!/usr/bin/python3
"""Square module."""

class Square:

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an interger')
        if size is not 0:
            raise ValueError('size must be >= 0')
        self.__size = size
