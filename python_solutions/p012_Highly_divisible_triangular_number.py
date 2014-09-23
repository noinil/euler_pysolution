#!/bin/env python

import sympy

n = 1
tri = n
factor_list = {}
m = 1                           # number of divisors
while True:
    m = 1
    n = n + 1
    tri = tri + n
    factor_list = sympy.factorint(tri)
    for i in factor_list.values():
        m = m * (i + 1)
    if m > 500:
        print(tri)
        break
