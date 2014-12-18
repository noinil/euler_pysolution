#!/usr/bin/env python3

import sympy as sp

def main(N):
    digi_factorial = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

    def df(n):
        return sum([digi_factorial[int(i)] for i in list(str(n))])

    bad_set = set()
    count = 0

    for i in range(2, N + 1):
        if i in bad_set:
            print(i, "is bad! ...")
            continue
        loc = [i]
        while True:
            t = df(loc[-1])
            if t in loc:
                break
            loc.append(t)
        l = len(loc)
        print(i, l)
        if l == 60:
            count += 1
        for j in range(l - 59, l):
            if j >= 0:
                bad_set.add(loc[j])

    print(" Totally ", count, "chains has 60 numbers.")


if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
