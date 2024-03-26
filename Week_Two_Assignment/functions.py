#!/usr/bin/python3


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
result = sum_all(10,40,50,60,50)

print(result)