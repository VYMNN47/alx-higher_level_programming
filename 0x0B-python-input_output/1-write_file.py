#!/usr/bin/python3
'''Defining write_file with two arguments'''

def write_file(filename="", text=""):
    '''reads filename with utf-8'''
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
