#!/bin/env python

import sympy as sp
import math

def sum_factorial(n):
    m = sp.factorial(n)
    return sum([int(i) for i in str(m)[:]])

if __name__ == "__main__":
    import sys
    N = sys.argv[1]

    print(sum_factorial(N))
