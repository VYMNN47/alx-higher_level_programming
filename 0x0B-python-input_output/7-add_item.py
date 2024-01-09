#!/usr/bin/python3
'''A script that adds all arguments to a Python list'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    o_dt = load_from_json_file('add_item.json')
except Exception:
    o_dt = []

o_dt.extend(arglist)
save_to_json_file(o_dt, 'add_item.json')
