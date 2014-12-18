#!/usr/bin/env python3

def p3(n):
    return n * (n + 1) // 2

def p4(n):
    return n * n

def p5(n):
    return n * (3 * n - 1) // 2

def p6(n):
    return n * (2 * n - 1)

def p7(n):
    return n * (5 * n - 3) // 2

def p8(n):
    return n * ( 3 * n - 2)

def main():
    import itertools as ittl
    idx = list(ittl.permutations([0,1,2,3,4]))
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    for i in range(30, 200):
        p = p3(i)
        if 999 < p < 10000 and str(p)[2] != '0':
            l3.append(p)
        if p >= 10000:
            break
    for i in range(30, 101):
        p = p4(i)
        if 999 < p < 10000 and str(p)[2] != '0':
            l4.append(p)
        if p >= 10000:
            break
    for i in range(20, 100):
        p = p5(i)
        if 999 < p < 10000 and str(p)[2] != '0':
            l5.append(p)
        if p >= 10000:
            break
    for i in range(20, 100):
        p = p6(i)
        if 999 < p < 10000 and str(p)[2] != '0':
            l6.append(p)
        if p >= 10000:
            break
    for i in range(20, 100):
        p = p7(i)
        if 999 < p < 10000 and str(p)[2] != '0':
            l7.append(p)
        if p >= 10000:
            break
    for i in range(10, 100):
        p = p8(i)
        if 999 < p < 10000 and str(p)[2] != '0':
            l8.append(p)
        if p >= 10000:
            break

    large_list = [l4, l5, l6, l7, l8]

    for i in l3:
        li = int(str(i)[:2])
        ri = int(str(i)[2:])
        print(i)
        for index in idx:
            listj = large_list[index[0]]
            listk = large_list[index[1]]
            listl = large_list[index[2]]
            listm = large_list[index[3]]
            listn = large_list[index[4]]
            for j in listj:
                lj = int(str(j)[:2])
                if lj != ri:
                    continue
                rj = int(str(j)[2:])
                print("  ", j)
                for k in listk:
                    lk = int(str(k)[:2])
                    if lk != rj:
                        continue
                    rk = int(str(k)[2:])
                    print("    ", k)
                    for l in listl:
                        ll = int(str(l)[:2])
                        if ll != rk:
                            continue
                        rl = int(str(l)[2:])
                        print("      ", l)
                        for m in listm:
                            lm = int(str(m)[:2])
                            if lm != rl:
                                continue
                            rm = int(str(m)[2:])
                            print("        ", m)
                            for n in listn:
                                ln = int(str(n)[:2])
                                if ln != rm:
                                    continue
                                rn = int(str(n)[2:])
                                print("          ", n)
                                if rn == li:
                                    print(i, j, k, l, m, n)
                                    print(i + j + k + l + m + n)
                                    return

if __name__ == '__main__':
    main()
