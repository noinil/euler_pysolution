#!/usr/bin/env python


def main(N):
    pat = {}
    def fun(m, n):
        if m <= n:
            return fun(m, m - 1) + 1
        if m == 1 and n == 0:
            return 0
        if (m, n) in pat.keys():
            return pat[(m, n)]
        count = 0
        for i in range(n, 0, -1):
            count += fun(m - i, i)
        pat[(m, n)] = count
        return count
    print(fun(N, N-1))


if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
