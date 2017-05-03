#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of"
greater = "and is greater than 5"
zero = "and is 0"
lesser = "and is less than 6 and not 0"

if number < 0:
    lnum = ((number * -1) % 10) * -1
else:
    lnum = number % 10
if lnum > 5:
    l = greater
elif lnum == 0:
    l = zero
else:
    l = lesser
print(s, number, "is", lnum, l)
