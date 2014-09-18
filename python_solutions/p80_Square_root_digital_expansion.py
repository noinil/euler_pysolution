#!/usr/bin/env python

def f(n):
    x, m = int(n ** 0.5), 1
    for i in range(0, 101):
        x *= 10
        m *= 10
        for j in range(9, -1, -1):
            y = x + j
            if y * y < m * m * n:
                break
        x = y
    print(n, x)
    return sum([int(i) for i in str(x)[0:100]])

def main():
    c = 0
    for i in range(1, 101):
        if round(i**0.5)**2 == i:
            print(i, "is square!")
        else:
            t = f(i)
            print(i, t)
            c += t
    print(c)

if __name__ == '__main__':
    main()
