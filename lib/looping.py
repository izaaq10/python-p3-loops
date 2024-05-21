#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >= 1:
        print (f"{i}")
        i -= 1
        print("Happy New Year!")
    pass
def square_integers(int_list):
    squared_numbers = []
    for n in int_list:
        squared_numbers.append(n ** 2)
    return squared_numbers

pass

def fizzbuzz():
    for i in range(1, 101):  
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
