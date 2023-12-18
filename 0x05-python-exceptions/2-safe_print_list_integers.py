#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y, z = 0, 0
    while y is not x:
        try:
            print('{:d}'.format(my_list[y]), end='')
            z += 1
        except (ValueError, TypeError):
            pass
        y += 1
    print()
    return c

