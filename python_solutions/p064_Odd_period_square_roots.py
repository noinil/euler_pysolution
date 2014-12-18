#!/usr/bin/env python3

import fractions as frac
from math import sqrt

def continued_fraction_ll(n):
    if is_square(n):
        return 0
    a0 = int(sqrt(n))
    i = frac.Fraction(1)
    r = frac.Fraction(-a0)
    p0 = [i, r]
    p = p0
    count = 0
    while True:
        i = p[0]
        r = p[1]
        # print("i =", i , "r=", r)
        h = float(i) * sqrt(n) + float(r)
        # print(h)
        m = int(1/h)
        # print("m =", m)
        i, r = i / (i**2 * n - r**2), (-r / (i**2 * n - r**2)) - m
        p = [i, r]
        # print(p)
        count += 1
        if p == p0:
            break
    return count

def is_square(n):
    from math import sqrt
    i = sqrt(n)
    if round(i)**2 == n:
        return True
    else:
        return False

def main():
    count = 0
    for i in range(1, 10001):
        p = continued_fraction_ll(i)
        print(i, p)
        if p % 2 == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
