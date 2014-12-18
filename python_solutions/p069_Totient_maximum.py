#!/usr/bin/env python3

import sympy as sp

def Totient(n):
    l = sp.primefactors(n)
    s = 1
    for i in l:
        s *= (i - 1)/i
    return s

def main(N):
    m = 0
    b = 0
    bad_set = {20}
    for i in range(2, N + 1):
        if i in bad_set:
            print(i, "is bad.")
            continue
        l = sp.primefactors(i)
        s = 1
        for j in l:
            s *= j / (j - 1)
            h = i
            while h <= N:
                h *= j
                bad_set.add(h)
        print(i, s)
        if m < s:
            m, b = s, i
    print("Max of n/phi(n) is: n =", b, ", n/phi = ", m)

if __name__ == '__main__':
    main(1000000)
