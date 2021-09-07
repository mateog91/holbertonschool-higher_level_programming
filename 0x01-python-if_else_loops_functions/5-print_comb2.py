#!/usr/bin/python3
for number in range(0, 99):
    if number < 98:
        print("{:02d}".format(number), end=", ")
print("{:02d}".format(number))
