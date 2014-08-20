#!/bin/env python

def a(m, n):
    return abs(m * m - n * n)

def b(m, n):
    return 2 * m * n

def c(m, n):
    return m * m + n * n

for m in range(1, 500):
    for n in range(1, 500):
        if a(m, n) + b(m, n) + c(m, n) == 1000:
            print(a(m, n) * b(m, n) * c(m, n))
            break
    else:
        continue
    break
