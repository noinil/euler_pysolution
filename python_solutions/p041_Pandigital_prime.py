#!/usr/bin/env python

def pandigital_list(n):
    import itertools
    if n <= 1 or n > 9:
        print(" n should be between 1 and 9! ")
        return
    funlist = []
    s = ''
    for i in range(1, n + 1):
        s = s + str(i)
    p = list(itertools.permutations(s))
    for i in p:
        s = ''
        for j in i:
            s = s + j
        funlist.append(int(s))
    return funlist

def main():
    import sympy
    import p37_Truncatable_primes as p37
    lucky_prime = 0
    plist = []
    for i in range(2, 10):
        plist = pandigital_list(i)
        for j in plist[:]:
            if p37.is_prime(j) and lucky_prime < j:
                lucky_prime = j
    print(lucky_prime)

if __name__ == '__main__':
    main()
