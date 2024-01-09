#!/usr/bin/python3
'''Contains the class Student'''

class Student:
    '''Info about the student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dict representation of a student instance'''
        try:
            for x in attrs:
                if type(x) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        own_dict = dict()
        for q, v in self.__dict__.items():
            if q in attrs:
                own_dict[q] = v
        return own_dict

    def reload_from_json(self, json):
        '''A func that replaces all attributes
        of the Student instance '''
        for q, v in json.items():
            if q in self.__dict__:
                self.__dict__[q] = v
