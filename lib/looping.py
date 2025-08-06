#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
    pass

def square_integers(numbers):
    # code goes here!
    return [number**2 for number in numbers]
    pass

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    pass
