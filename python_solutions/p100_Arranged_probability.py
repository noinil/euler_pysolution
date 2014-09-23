#!/usr/bin/env python

import sympy as sp

def main(N):
    n = 1
    while True:
        n += 1
        # print(n)
        t = 0.5 * (1 + (1 + 2 * n * n - 2 * n) ** 0.5)
        # if t.is_integer():
        #     m = round(t)
            # fcts0 = sp.factorint(n * (n - 1))
            # fcts0[2] = fcts0[2] - 1
            # for i in range(-2, 2, 1):
            #     v = m + i
                # fcts1 = sp.factorint(v * (v - 1))
                # if fcts0 == fcts1:
                #     print("aha!", n, v)
                #     return 0
                # if 2 * v * (v - 1) == n * (n - 1):
                #     print("aha!", n, v)
                #     return 0
        m = round(t)
        for i in range(-2, 3, 1):
            v = m + i
            if 2 * v * (v - 1) == n * (n - 1):
                print("aha!", n, v)

        if n > N:
            return 0


if __name__ == '__main__':
    main(10**5)
