#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    '''if an object is a subclass of a class return True
    if not False.'''
    return isinstance(obj, a_class)
