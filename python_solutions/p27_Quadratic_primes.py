#!/usr/bin/env python

def prime_producer(a, b):
    import sympy
    n = 0
    while True:
        f = n**2 + a * n + b
        if f <= 0 or len(sympy.primefactors(f)) > 1:
            break
        n = n + 1
    return n

def main():
    max_pnum = 0
    i, j = 0, 0
    for a in range(-1000, 1001, 1):
        for b in range(2, 1001, 1):
            p_num = prime_producer(a, b)
            print(a, b, p_num)
            if p_num > max_pnum:
                max_pnum = p_num
                i, j = a, b
    print(i, "x", j, "=", i * j)

if __name__ == '__main__':
    main()
