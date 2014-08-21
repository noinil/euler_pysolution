#!/usr/bin/env python

def main(n):
    a , b = 0, 1
    count = 0
    while True:
        a, b = b, a+b
        count = count + 1
        if a // 10**(n - 1) > 0:
            print(count)
            break

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])

    main(n)
