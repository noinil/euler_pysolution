#!/usr/bin/env python

def main():
    p = [1, 1, 2]
    n = 2
    while True:
        n += 1
        pt = 0
        i = 0
        k = 1
        while True:
            gk = k * (3 * k - 1) // 2
            i = n - gk
            if i < 0:
                break
            pt += (-1) ** (k * k + 1) * p[i]
            k = -1 * k if k > 0 else 1 - k
        p.append(pt)
        if pt % 1000000 == 0:
            print("finally, n =", n, "partition =", pt)
            break
    return 0

if __name__ == '__main__':
    main()
