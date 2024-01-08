#!/usr/bin/python3
'''Module for lookup'''

def lookup(obj):
    '''function that returns the list of available attributes
    Args:
        obj: the object to list.

    Return: list of attributes
    '''

    return dir(obj)
