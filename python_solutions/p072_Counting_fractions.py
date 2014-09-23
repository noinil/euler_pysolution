#!/usr/bin/env python

# import fractions as fr
import sympy as sp

def main(N):
    count = 0
    for i in range(2, N + 1):
        print(i)
        s = i
        for t in sp.primefactors(i):
            s *= (t - 1) / t
        count += int(s)
    print(count)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])

    main(N)
