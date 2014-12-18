#!/usr/bin/env python3

def main():
    import sympy as sp
    plist = list(sp.primerange(999, 10000))

    for i in plist:
        for j in plist[plist.index(i)+1:]:
            k = 2 * j - i
            if k in plist:
                digi_set_i = set(str(i))
                digi_set_j = set(str(j))
                digi_set_k = set(str(k))
                if digi_set_i == digi_set_j == digi_set_k :
                    print(i, j, k, sep='')


if __name__ == '__main__':
    main()
