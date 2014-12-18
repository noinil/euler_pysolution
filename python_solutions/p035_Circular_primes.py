#!/usr/bin/env python3

def is_prime(n):
    import sympy
    if len(sypmy.primefactors(n)) == 1:
        return 1
    else:
        return 0

def main(n):
    import sympy
    import itertools
    p_list = list(sympy.primerange(1, n+1))
    lucky_set = {2}
    for i in p_list:
        if i in lucky_set:
            continue
        local_list = [i]
        digits = str(i)
        n_order = len(digits)
        for j in digits[:]:
            if int(j)%2==0:
                break
        else:
            for k in range(0,n_order):
                s = digits[k:] + digits[:k]
                tmp_int = int(s)
                if tmp_int in p_list:
                    local_list.append(tmp_int)
                else:
                    break
            else:
                for m in local_list:
                    lucky_set.add(m)

    print(sorted(lucky_set))
    print(len(lucky_set))


if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
