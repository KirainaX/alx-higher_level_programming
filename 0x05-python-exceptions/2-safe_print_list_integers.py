#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''count = 0
    i = 0
    try:
        while count < x:
            if isinstance(my_list, int):
                print(my_list[count], end="")
                count += 1
            else:
                continue
    except IndexError as err:
        print("IndexError: ", err)
    print("")
    return count'''
    i, c = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return c
