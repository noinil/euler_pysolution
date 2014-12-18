#!/usr/bin/env python3

def main():
    a = 2**457 % 10**10
    b = 2**1000 % 10**10
    c = 28433
    d = 1
    e = 1
    for i in range(0, 7830):
        e = (e * b) % 10**10
    final = (e * a * c) % 10**10 + 1
    print(final)

if __name__ == '__main__':
    main()
