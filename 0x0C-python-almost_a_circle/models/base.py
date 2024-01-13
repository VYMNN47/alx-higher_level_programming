#!/usr/bin/python3
'''Base class.'''

class Base:
    '''A representation of the base of our OOP'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
