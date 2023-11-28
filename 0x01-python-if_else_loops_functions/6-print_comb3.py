#!/usr/bin/python3
for x in range(10):
    for y in range(x, 10):
        if x < y:
            print("{:d}{:d}".format(x, y),
                    end="\n" if x == 8 and y == 9 else ", ")
