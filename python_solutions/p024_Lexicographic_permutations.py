#!/usr/bin/env python

import sympy

def main():
    import sys
    N = int(sys.argv[1]) - 1
    digits = [i for i in range(0, 10)]
    nodes = [sympy.factorial(i) for i in range(9, 0, -1)]
    lucky_number = []

    for i in nodes:
        r = N // i
        N = N % i
        lucky_number.append(digits.pop(r))

    for i in lucky_number:
        print(i, end = '')
    print(digits[0])

def main_2():
    import sys
    N = int(sys.argv[1]) - 1

    import itertools
    m = [i for i in range(0,10)]
    n = list(itertools.permutations(m))
    print(n[N])

if __name__ == '__main__':
    main()
    main_2()
