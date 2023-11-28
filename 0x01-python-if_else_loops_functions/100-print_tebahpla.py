#!/usr/bin/python3
for x in range(25, -1, -1):
    v = x + ord('A')
    if x % 2 == 1:
        v += 32
    print(f"{v:c}", end="")
