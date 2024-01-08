#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    def __new__(cls, *agrs, **kwargs):
        return super(MyInt, cls).__new__(cls, *agrs, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
