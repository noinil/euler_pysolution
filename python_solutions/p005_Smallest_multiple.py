#!/bin/env python

import sympy

def p_factor_table(n):
    pfs = sympy.primefactors(n)
    pf_tbl = {}
    for i in pfs:
        pf_tbl[i] = 0
        m = n
        while m % i == 0:
            m = m // i
            pf_tbl[i] = pf_tbl[i] + 1
    return pf_tbl

if __name__ == "__main__":
    max = 20
    multiple = 1

    # get the global prime_factor table
    global_tbl = {}
    for i in range(2, max+1):
        local_tbl = p_factor_table(i)
        for j in local_tbl.keys():
            if j not in global_tbl or global_tbl[j] < local_tbl[j]:
                global_tbl[j] = local_tbl[j]

    # multiply every prime factor
    for i, j in global_tbl.items():
        multiple = multiple * i ** j

    print(multiple)
