#!/usr/bin/python3
def remove_char_at(str, n):
    _str = ""
    for x, y in enumerate(str):
        if x != n:
            _str += y
    return _str
