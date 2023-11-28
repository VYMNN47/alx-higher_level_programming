#!/usr/bin/python3
for x in range(100):
    print("{:02d}".format(x), end="\n" if x == 99 else ", ")
