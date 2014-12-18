#!/usr/bin/env python3

import p37_Truncatable_primes as p37

def main():
    i = 1
    x = 1
    np = 0
    N = 1
    while True:
        i = i + 1
        for j in range(0,3):
            x = x + 2 * i - 2
            if p37.is_prime(x):
                np = np + 1
        x = x + 2 * i - 2
        N = N + 4
        if np / N < 0.1:
            print(i * 2 - 1)
            return

if __name__ == '__main__':
    main()
