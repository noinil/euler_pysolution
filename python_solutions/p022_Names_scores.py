#!/bin/env python3

def alpha_value(s):
    return sum([ord(i) - ord('A') + 1 for i in s])


with open('../data/p22_names.txt', 'r') as f:
    str = f.readlines()[0]
    quoted_names = str.split(sep = ',')
    names = [i[1:-1] for i in quoted_names]

names.sort()
print(sum([ (names.index(s) + 1) * alpha_value(s) for s in names]))
