#!/usr/bin/env python

import math
import sympy as sp
import p37_Truncatable_primes as p37

def Totient(n):
    l = sp.primefactors(n)
    s = n
    for i in l:
        s *= (i - 1) / i
    return int(s)


def main(N):
    m = 1.0008
    b = 0
    td = {}
    bad_set = set()
    for i in range(int(N * 0.80), int(N*0.9)+1):
        # if i in bad_set:
        #     continue
        # if p37.is_prime(i):
        #     continue
        # if i in td.keys():
        #     t = td.pop(i)
        # else:
        #     t = Totient(i)
        t = Totient(i)
        s = i / t
        if m <= s:
            # for j in sp.primefactors(i):
            #     h = i
            #     while h <= N:
            #         h *= j
            #         bad_set.add(h)
            #         if h in td.keys():
            #             td.pop(h)
            continue
        # for j in sp.primefactors(i):
        #     h, g = i, t
        #     while h <= N:
        #         h *= j
        #         g *= j
        #         if h in td.keys():
        #             continue
        #         td[h] = g
        st = list(str(t))
        si = list(str(i))
        st.sort()
        si.sort()
        if si == st:
            m, b = s, i
            print(i, t, m)
    print("Best is: n =", b, ", n/phi = ", m)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
    # print(Totient(N))
