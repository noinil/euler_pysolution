#!/usr/bin/env python3

def main(N):
    import math
    import fractions as fr
    c = 1/3
    d = 1/2
    bad = set()
    for i in range(5, N + 1):
        print(i)
        s = c * i
        t = d * i
        sf = math.ceil(s)
        tf = int(t)
        for f in range(sf, tf + 1):
            if c < f / i < d:
                bad.add(fr.Fraction(f, i))
    print(len(bad))


if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
