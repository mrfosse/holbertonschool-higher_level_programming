#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    s = "is positive"
elif number < 0:
    s = "is negative"
else:
    s = "is zero"
print(number, s)
