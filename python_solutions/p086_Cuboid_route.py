#!/usr/bin/env python

def int_cube(x0, y0):
    z2 = x0 * x0 - y0 * y0
    z1 = round(z2 ** 0.5)
    if z1 * z1 == z2:
        return z1
    else:
        return 0

def main(N):
    count = 0
    n = 1
    while True:
        n += 1
        for i in range(n + 1, int(5**0.5 * n) + 1):
            j = int_cube(i, n)
            if j == 0:
                continue
            for a in range(1, n + 1):
                b = j - a
                if 1 <= a <= b <= n:
                    count += 1
        if count >= N:
            break
    print(n)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
