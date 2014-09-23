#!/usr/bin/env python

def main():
    import sympy as sp
    plist = list(sp.primerange(1, 1000000))
    s, t = 0, 0
    l = 0
    best_l = 1
    best = 1
    best_s = 0
    for i in range(1, len(plist)):
        p = plist[i]
        tmp = 0
        for s in range(0, best_l):
            tmp = tmp + plist[s]
        if tmp > p:
            continue
        for s in range(0, i-1):
            if plist[s] > p // best_l:
                break
            local_sum = 0
            for t in range(s, i):
                local_sum = local_sum + plist[t]
                if local_sum > p:
                    l = t - s + 1
                    break
                if local_sum == p:
                    l = t - s + 1
                    print(p, l, s)
                    if l > best_l:
                        best_l = l
                        best = p
                        best_s = s
                    break
            if l <= best_l and local_sum > p:
                break
            if local_sum == p:
                break

    print("The longest one:", best, best_l)


if __name__ == '__main__':
    main()
