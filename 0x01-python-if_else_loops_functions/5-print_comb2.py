#!/usr/bin/python3
for x in range(100):
    print(f"{:02d}"{x}, end="\n" if x == 99 else ", ")
