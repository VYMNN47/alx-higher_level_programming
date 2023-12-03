#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divbytwo = []
    for x in my_list:
        if (x % 2) == 0:
            divbytwo.append(True)
        else:
            divbytwo.append(False)
        return divbytwo
