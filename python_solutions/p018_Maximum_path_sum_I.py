#!/usr/bin/env python

import math

mat = []
row = []

with open('../data/p018_triangle.data', 'r') as f:
    for line in f:
        for i in line.split():
            row.append(int(i))
        mat.append(row[:])
        row.clear()

ans = 0

for i in range(0, int(math.pow(2, len(mat)-1)) ):
    index_str = bin(i)[2:]
    while len(index_str) < len(mat) - 1:
        index_str = '0' + index_str
    indx = 0
    tot = int(mat[0][0])
    for j in range(0, len(index_str)):
        indx = indx + int(index_str[j])
        tot = tot + mat[j + 1][indx]
        # print(mat[j + 1][indx], end=' ')

    ans = tot if ans < tot else ans
    # print(ans)

print(ans)
