#!/usr/bin/python3
'''defining to_json_string function'''

import json

def to_json_string(my_obj):
    '''returns the JSON representation of an obj'''
    return json.dumps(my_obj)
