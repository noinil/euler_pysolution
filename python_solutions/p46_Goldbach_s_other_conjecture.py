#!/usr/bin/env python

import p37_Truncatable_primes as p37

def is_square(n):
    import math
    i = int(math.sqrt(n))
    if i * i == n:
        return True
    else:
        return False

def main():
    import sympy

    plist = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    i = 33
    while True:
        i = i + 2
        if p37.is_prime(i):
            plist.append(i)
        else:
            local_list = [(i - j) // 2 for j in plist]
            for k in local_list:
                if is_square(k):
                    print(i, "woo...")
                    break
            else:
                print(i, "is the final number.")
                break


if __name__ == '__main__':
    main()
