#!/usr/bin/env python3
import ipdb


def print_fibonacci(length):
    fib1 = 0
    fib2 = 1
    fib_list = []
    if length <= 0:
        print(fib_list)
    elif length == 1:
        fib_list = [fib1]
        print(fib_list)
    elif length == 2:
        fib_list = [fib1, fib2]
        print(fib_list)
    else:
        fib_list = [fib1, fib2]
        while len(fib_list) < length:
            fib2 = fib_list[-2]
            fib1 = fib_list[-1]
            fib3 = fib1 + fib2
            fib_list.append(fib3)
        print(fib_list)
