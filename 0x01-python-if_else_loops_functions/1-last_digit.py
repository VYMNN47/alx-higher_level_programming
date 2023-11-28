#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdt = number % 10 if number > 10 else number % -10
print(f"Last digit of {number} is {lastdt} and is ")
if lastdt > 5:
    print("greater than 5")
elif lastdt == 0:
    print("0")
else:
    print("less than 6 and not 0")
