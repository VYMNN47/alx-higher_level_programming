#!/usr/bin/python3
'''A function that inserts a line of text to a file'''

def append_after(filename="", search_string="", new_string=""):
    '''a function that inserts a line of text to a file'''
    with open(filename, 'r', encoding='utf-8') as file:
        line_list = []
        while true:
            line = file.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line_list)
