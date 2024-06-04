#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if (length) == 0:
            print(fib)
    elif length == 1:
            fib.append(0)
            print(fib)
    elif length == 2:
            for num in range(length):
                fib.append(num)
            print(fib)
    elif length == 10:
            fib = [0,1]
            for num in range(2,length): 
                fib.append(fib[-1] + fib[-2])
            print(fib)