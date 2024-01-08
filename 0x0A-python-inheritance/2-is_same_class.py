#!/usr/bin/python3
'''Module for is_same_class.'''


def is_same_class(obj, a_class):
    '''if an object is exactly an instance of a class returns True.'''
    return type(obj) == a_class
