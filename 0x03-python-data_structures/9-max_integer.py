#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        high_num = my_list.copy()
        high_num.sort()
        return high_num(-1)
