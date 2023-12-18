#!/usr/bin/python3
def safe_print_integer(value):
    try:
        while isinstance(value, int):
            print("{:d}".format(value), end="")
            print("")
            return True
    except (TypeError, ValueError):
        return False
