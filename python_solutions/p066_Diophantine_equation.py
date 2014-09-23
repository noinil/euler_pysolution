#!/usr/bin/env python

import fractions as frac
from math import sqrt

def continued_fraction_ll(n):
    ll = []
    a0 = int(sqrt(n))
    ll.append(a0)
    if is_square(n):
        return ll

    i = frac.Fraction(1)
    r = frac.Fraction(-a0)
    p0 = [i, r]
    p = p0
    while True:
        i = p[0]
        r = p[1]
        # print("i =", i , "r=", r)
        h = float(i) * sqrt(n) + float(r)
        # print(h)
        m = int(1/h)
        ll.append(m)
        # print("m =", m)
        i, r = i / (i**2 * n - r**2), (-r / (i**2 * n - r**2)) - m
        p = [i, r]
        # print(p)
        if p == p0:
            break
    return ll

def is_square(n):
    from math import sqrt
    i = sqrt(n)
    if round(i)**2 == n:
        return True
    else:
        return False

def Pell_solution(n):
    if is_square(n):
        return -1
    h0, h1 = 0, 1
    k0, k1 = 1, 0
    ll = continued_fraction_ll(n)
    a = ll.pop(0)
    lol = len(ll)
    i = 0
    while True:
        h1, h0 = a * h1 + h0, h1
        k1, k0 = a * k1 + k0, k1
        if h1 ** 2 - n * k1 ** 2 == 1:
            # print(h1, "^2 - ", n, "x", k1, "^2 = 1")
            # print("sqrt of", n, "~", "h1/k1 = ", h1/k1)
            break
        a = ll[i]
        i = (i + 1) % lol
    return h1

def main(N):
    la = 0
    x = 0
    for i in range(2, N):
        t = Pell_solution(i)
        print(i, t)
        if la < t:
            la = t
            x = i
    print(x)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
    # print(continued_fraction_ll(N))
    # print(Pell_solution(N))
