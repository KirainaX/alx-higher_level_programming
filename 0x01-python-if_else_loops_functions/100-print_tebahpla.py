#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2) != 0:
        i = i - 32
    c = chr(i)
    print(c, end="")