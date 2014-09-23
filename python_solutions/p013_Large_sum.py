#!/bin/env python

a = []
n = 1111111111111111111111111111111111111111

with open('../data/p13_digits.data', 'r') as f:
    for lines in f:
        n = int(lines)
        a.append(n)

s = sum(a)
print(str(s)[:10])
