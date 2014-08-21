#!/bin/env python

import sympy

def fac_list(n):
    f_list = [1]
    prime_fac_dict = sympy.factorint(n)
    for i, j in prime_fac_dict.items():
        f_list.extend([a * i ** k for a in f_list[:] for k in range(1, j+1)])
    f_list.remove(n)
    return f_list

def fac_sum(n):
    return sum(fac_list(n))

a =[]

if __name__ == "__main__":
    N = 10000
    for i in range(2, N+1):
        j = fac_sum(i)
        if j > i == fac_sum(j):
            a.append(i)
            a.append(j)

    print(sum(a))
