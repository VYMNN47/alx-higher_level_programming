#!/usr/bin/python3
'''Module for MyList class.'''


class MyList(list):
    '''Printing sorted list.'''
    def print_sorted(self):
        print(sorted(self))
