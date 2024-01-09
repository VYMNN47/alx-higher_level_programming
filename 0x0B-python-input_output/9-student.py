#!/usr/bin/python3
'''Contains the class Student'''

class Student:
    '''Info about the student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns a dict representation of a student instance'''
        return self.__dict__
