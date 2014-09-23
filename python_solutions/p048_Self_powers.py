#!/usr/bin/env python

def last_10_multiply(n, m):
    if n > 10**10:
        n = n % 10**10
    if m > 10**10:
        m = m % 10**10
    return (n * m) % 10**10

def mimi(n):
    s = 1
    for i in range(1, n + 1):
        if s < 10**10:
            s = s * n
        else:
            s = last_10_multiply(s, n)
    return s

def main():
    s = 0
    for i in range(1, 1001):
        s = s + mimi(i)
        if s > 10**10:
            s = s % 10**10
    print(s)


if __name__ == '__main__':
    main()
