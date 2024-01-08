#!/usr/bin/python3
"""
Contains the class MyInt
"""

class MyInt(int):
    """Switch between the = and !="""

    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """What was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """What was == is now !="""
        return int(self) == other

