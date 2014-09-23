#!/bin/env python

def is_palindrome(x):
    s = str(x)
    if s[::-1] == s:
        return True
    else:
        return False

if __name__ == "__main__":
    max = 0
    n = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            n = i * j
            if is_palindrome(n):
                break
        max = n if max < n else max

    print(max)
