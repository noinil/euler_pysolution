#!/usr/bin/env python3

import sympy as sp

def fun(n):
    if n == 1:
        return 1
    factor_list = [1]
    for i, j in sp.factorint(n).items():
        for s in factor_list[:]:
            for t in range(1, j + 1):
                factor_list.append(s * i ** t)
    factor_list.remove(n)
    return sum(factor_list)

def main(N):
    wl = {}
    best = 0
    besti = 0
    for i in range(1, N):
        # print(i)
        if i in wl:
            continue
        j = i
        loc_list = []
        while True:
            j = fun(j)
            if j in wl or j > N or j == 1 or j == i or j in loc_list:
                break
            loc_list.append(j)
        if j > N:
            for tmp in loc_list:
                wl[tmp] = -1
            continue
        elif j == 1:
            for tmp in loc_list:
                wl[tmp] = 0
            continue
        elif j in wl:
            for tmp in loc_list:
                wl[tmp] = wl[j]
            continue
        elif j in loc_list and j != i:
            continue
        else:
            loc_list.append(i)
            c = len(loc_list)
        for tmp in loc_list:
            wl[tmp] = c
        print(i, c, loc_list)
        if best == 0 or best < c:
            # print(i, "is the best one", c, loc_list)
            best = c
            besti = i
    print("finally ", besti, best)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
