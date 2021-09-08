#!/usr/bin/python3
def fizzbuzz():
    for number in range (1, 101):
        if number % 3 == 0:
            if number % 5 == 0:
                print_value = "FizzBuzz"
            else:
                print_value = "Fizz"
        elif number % 5 == 0:
            print_value = "Buzz"
        else:
            print_value = number
        print(print_value, end=" ")
