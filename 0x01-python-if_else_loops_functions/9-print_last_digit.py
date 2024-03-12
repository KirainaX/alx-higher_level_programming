#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastN = -number % 10
    else:
        lastN = number % 10

    print("{:d}".format(lastN), end="")
    return lastN
