#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    text = "and is greater than 5"
elif last_digit == 0:
    text = "and is 0"
else:
    text = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, last_digit, text))