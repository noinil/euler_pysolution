#!/usr/bin/env python3

def u(n):
    return sum( (-n) ** i for i in range(0, 11))

def lagrange_interpolation(y):
    xn = len(y) + 1
    for x in range(1, xn + 1):
        u = 0
        for i in range(0, xn - 1):
            fac1, fac2 = 1, 1
            for j in range(0, xn - 1):
                if j == i:
                    continue
                fac1 *= (x - j - 1)
                fac2 *= (i - j)
            u += y[i] * fac1 // fac2
        print(u, end = ' ')
    print()
    return u

def main():
    bop = 0
    y_list = [u(i) for i in range(1, 11)]
    print(y_list)
    for i in range(1, 11):
        bop += lagrange_interpolation(y_list[:i])
    print(bop)

if __name__ == '__main__':
    main()
