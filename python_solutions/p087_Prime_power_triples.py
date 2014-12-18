#!/usr/bin/env python3

import sympy

def main(N):
    lim2 = round(N ** 0.5) + 1
    lim3 = round(N ** (1 / 3)) + 1
    lim4 = round(N ** (1 / 4)) + 1
    pl = list(sympy.primerange(1, lim2))
    pt = set()
    for i in pl:
        s = i ** 4
        if s > N:
            break
        for j in pl:
            s = j ** 3 + i ** 4
            if s > N:
                break
            for k in pl:
                s = k ** 2 + j ** 3 + i ** 4
                if s > N:
                    break
                pt.add(s)

    print(len(pt))

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
