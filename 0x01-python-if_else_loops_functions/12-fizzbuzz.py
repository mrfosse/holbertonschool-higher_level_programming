#!/usr/bin/python3
def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(num), end="")
        num = num + 1
