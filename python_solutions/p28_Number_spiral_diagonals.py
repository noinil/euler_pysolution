#!/usr/bin/env python

def main():
    diag = []
    total = 1
    n = 1
    for i in range(1, 501):
        for j in range(1,5):
            n = n + 2 * i
            total = total + n
    print(total)

if __name__ == '__main__':
    main()
