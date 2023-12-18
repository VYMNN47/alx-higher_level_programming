#!/usr/bin/python3
def magic_calculation(a, b):
    x = 0
    for e in range(1, 3):
        try:
            if e > a:
                raise Exception('Too far')
            x = x + a ** b / x
        except Exception:
            x = a + b
            break
    return x 
