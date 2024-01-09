#!/usr/bin/python3
'''defining from_json_string function'''

import json

def from_json_string(my_str):
    '''returns JSON str to an Object'''
    return json.loads(my_str)
