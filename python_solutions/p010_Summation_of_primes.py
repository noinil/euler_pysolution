#!/bin/env python

import sympy

N = 2000000
b = 0
s = 0
i = 1

while b < N:
    s = s + b
    b = sympy.prime(i)
    i = i + 1

print(s)
