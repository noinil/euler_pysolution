#!/usr/bin/env python3

def is_prime(i):
    import sympy
    if len(sympy.primefactors(i)) == 1 and sympy.primefactors(i)[0] == i:
        return True
    else:
        return False

def is_truncatable(n):
    s = str(n)
    for i in range(len(s), 0, -1):
        m = int(s[:i])
        if not is_prime(m):
            return False
        m = int(s[i-1:])
        if not is_prime(m):
            return False
    else:
        return True

def main():
    import sympy
    lucky_set = set()
    i = 5
    while True:
        m = sympy.prime(i)
        if is_truncatable(m):
            lucky_set.add(m)
        if len(lucky_set) == 11:
            break
        i = i + 1

    print(lucky_set)
    print(sum(lucky_set))

if __name__ == '__main__':
    main()
    # print(is_truncatable(83))
