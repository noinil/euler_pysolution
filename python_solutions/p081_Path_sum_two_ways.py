#!/usr/bin/env python3

def main():
    mat = []
    lm = []
    with open("../data/p81_matrix.txt", 'r') as fmat:
        for line in fmat:
            for i in line.split(','):
                lm.append(int(i))
            mat.append(lm[:])
            lm.clear()
    L = len(mat)
    print(mat[L-1][L-1])
    for i in range(1, L):
        mat[0][i] += mat[0][i - 1]
        mat[i][0] += mat[i - 1][0]
        for m in range(1, i):
            n = i - m
            a, b = mat[m-1][n], mat[m][n-1]
            mat[m][n] += a if a < b else b
            # print(m, n)
    for i in range(L, 2 * L - 1):
        for m in range(i - L + 1, L):
            n = i - m
            a, b = mat[m-1][n], mat[m][n-1]
            mat[m][n] += a if a < b else b
            # print(m, n)
    print(mat[L-1][L-1])

if __name__ == '__main__':
    main()
