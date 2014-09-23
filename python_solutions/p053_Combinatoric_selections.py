#!/usr/bin/env python

def combination(n, r):
    from sympy import factorial as fc
    return fc(n) / fc(r) / fc(n - r)

def main():
    N = 1000000
    sm = 15
    count = 0
    for i in range(23, 101):
        for j in range(1, sm+2):
            if combination(i, j) > N:
                sm = j
                count = count + (i - j - j + 1)
                break
    print(count)

if __name__ == '__main__':
    main()
