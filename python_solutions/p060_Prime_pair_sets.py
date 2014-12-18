#!/usr/bin/env python3

from p37_Truncatable_primes import is_prime as isp

def ccc(m, n):
    sm = str(m)
    sn = str(n)
    mn = int(sm+sn)
    nm = int(sn+sm)
    if isp(mn) and isp(nm):
        return True
    else:
        return False

def main():
    import sympy as sp
    pl1 = list(sp.primerange(3, 10000))
    pl11 = [i for i in pl1 if i % 3 == 1 or i % 3 == 0]
    pl12 = [i for i in pl1 if i % 3 == 2 or i % 3 == 0]

    plen = len(pl1)

    best = 1111111111110
    for a in pl1:
        print(a)
        p_loc_a = []
        for b in pl1:
            if b < a:
                continue
            if ccc(a, b):
                p_loc_a.append(b)
        for b in p_loc_a:
            p_loc_b = []
            for c in p_loc_a:
                if c < b:
                    continue
                if ccc(b, c):
                    p_loc_b.append(c)
            for c in p_loc_b:
                p_loc_c = []
                for d in p_loc_b:
                    if d < c:
                        continue
                    if ccc(c, d):
                        p_loc_c.append(d)
                for d in p_loc_c:
                    for e in p_loc_c:
                        if e < d:
                            continue
                        if ccc(d, e):
                            print(a, b, c, d, e)
                            s = a + b + c + d + e
                            print(s)
                            if s < best:
                                best = s
    print("best is ", best)

if __name__ == '__main__':
    main()
