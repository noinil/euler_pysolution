#!/usr/bin/env python

def is_triangle(n):
    from math import sqrt
    i = int(sqrt(8 * n + 1))
    if i * i == n * 8 + 1:
        return True
    else:
        return False

def is_pentagonal(n):
    from math import sqrt
    i = int(sqrt(24 * n + 1))
    if i * i == n * 24 + 1 and i % 3 == 2 and i % 2 == 1:
        return True
    else:
        return False

def main():
    i = 144
    while True:
        n = i * (2 * i - 1)
        if is_triangle(n) and is_pentagonal(n):
            print(n)
            break
        else:
            print(i)
        i = i + 1


if __name__ == '__main__':
    main()
