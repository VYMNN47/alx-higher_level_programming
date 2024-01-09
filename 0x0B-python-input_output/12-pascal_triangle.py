#!/usr/bin/python3
'''defining function'''

def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal’s triangle of n'''
    if i <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != i:
        tri = trian[-1]
        temp = [1]
        for x in range(len(tri) - 1):
            temp.append(tri[x] + tri[x + 1])
        temp.append(1)
        triangle.append(temp)
    return (triangle)
