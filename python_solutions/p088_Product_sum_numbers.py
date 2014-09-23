#!/usr/bin/env python

import sympy

def is_prime(i):
    if len(sympy.primefactors(i)) == 1 and sympy.primefactors(i)[0] == i:
        return True
    else:
        return False

def main(N):
    ps_set = set()              # Product-Sum number list
    k_list = [i for i in range(2, N + 1)]
    k_for_every_i = {2:{1}, 3:{1}}
    i = 3
    while len(k_list) > 0:
        i += 1
        if is_prime(i):
            k_for_every_i[i] = {1}
            continue
        local_k_dl = set()
        for f in range(2, int(i ** 0.5) + 1): # f : factor
            m, n = i // f, i % f
            if f > m:
                break
            if n == 0:
                k = i - m - f + 2
                local_k_dl.add(k)
                for km in k_for_every_i[m]:
                    k1 = k - 1 + km
                    local_k_dl.add(k1)
                for kf in k_for_every_i[f]:
                    k1 = k - 1 + kf
                    local_k_dl.add(k1)
                for km in k_for_every_i[m]:
                    for kf in k_for_every_i[f]:
                        k1 = k - 2 + kf + km
                        local_k_dl.add(k1)
        for k in local_k_dl:
            if k in k_list:
                k_list.remove(k)
                ps_set.add(i)
        print(i, "k_list =    ", local_k_dl)
        k_for_every_i[i] = local_k_dl
        print("len of k_list = ", len(k_list))
    print("set = ", ps_set)
    print(sum(ps_set))

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
