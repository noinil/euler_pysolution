#!/usr/bin/env python

import sympy

def main():
    prime_list = []
    def is_prime(i):
        if i in prime_list:
            return True
        if len(sympy.primefactors(i)) == 1 and sympy.primefactors(i)[0] == i:
            prime_list.append(i)
            return True
        else:
            return False
    psum_dic = {}
    def fun(m, n):
        if n == 1 or m == 1:
            return 0
        if m == 2:
            return 1
        if m <= n:
            if is_prime(m):
                return fun(m, m - 1) + 1
            else:
                return fun(m, m - 1)
        if (m, n) in psum_dic.keys():
            return psum_dic[(m, n)]
        count = 0
        for i in range(n, 1, -1):
            if is_prime(i):
                count += fun(m - i, i)
        psum_dic[(m, n)] = count
        return count
    # print(fun(N, N - 1))
    s = 10
    while True:
        s += 1
        t = fun(s, s - 1)
        print(s, t)
        if t >= 5000:
            print("Holy S! ", s)
            return 0

if __name__ == '__main__':
    main()
