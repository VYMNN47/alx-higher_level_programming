#!/usr/bin/python3
'''Base class.'''
from json import dumps, loads
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Json a dict so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
