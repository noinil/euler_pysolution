#!/usr/bin/env python

def is_palindrome_10(x):
    s = str(x)
    if s[::-1] == s:
        return True
    else:
        return False

def is_palindrome_2(x):
    s = bin(x)[2:]
    if s[::-1] == s:
        return True
    else:
        return False


def main(n):
    ss = 0
    for i in range(1, n + 1):
        if is_palindrome_10(i) and is_palindrome_2(i):
            ss = ss + i
    print(ss)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
