#!/bin/env python

mat = []
row = []
multi = 1

with open('../data/p11_grid.data', 'r') as f:
    for lines in f:
        row.clear()
        for s in lines.split():
            row.append(int(s))
        mat.append(row[:])

m = 1
for i in range(0, 20):
    for j in range(0, 20):
        if j < 17:
            m = mat[i][j] * mat[i][j+1] * mat[i][j+2] * mat[i][j+3]
            multi = m if multi < m else multi
        if j < 17 and i < 17:
            m = mat[i][j] * mat[i+1][j+1] * mat[i+2][j+2] * mat[i+3][j+3]
            multi = m if multi < m else multi
        if i < 17:
            m = mat[i][j] * mat[i+1][j] * mat[i+2][j] * mat[i+3][j]
            multi = m if multi < m else multi
        if j < 17 and i > 2:
            m = mat[i][j] * mat[i-1][j+1] * mat[i-2][j+2] * mat[i-3][j+3]
            multi = m if multi < m else multi

print(multi)
