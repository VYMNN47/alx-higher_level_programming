#!/usr/bin/python3
'''defining function'''

def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal’s triangle of n'''
    if i <= 0:
        return []

    trian = [[1]]
    while len(trian) != i:
        x = trian[-1]
        temp = [1]
        for e in range(len(x) - 1):
            temp.append(x[e] + x[e + 1])
        temp.append(1)
        trian.append(temp)
    return trian
