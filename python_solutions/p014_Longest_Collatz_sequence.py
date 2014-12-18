#!/bin/env python3

N = 1000000

def collatz(n):
    i = 1
    while n > 1:
        n = n//2 if n % 2 == 0 else 3 * n + 1
        i = i + 1
    return i

length = 0
n = 0
m = 0                           # store the number with the longest chain
for i in range(2, N):
    n = collatz(i)
    if length < n:
        length = n
        m = i

print("Finally, the number with the longest chain is :", m)

# Answer: 837799
