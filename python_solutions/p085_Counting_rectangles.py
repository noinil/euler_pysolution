#!/usr/bin/env python3

def main(N):
    cc = 100000
    area = 0
    for i in range(1, 100):
        for j in range(i, 2010):
            ni = i * (i + 1) // 2
            nj = j * (j + 1) // 2
            s = ni * nj - N
            print(i, j, ni, nj, ni * nj, s)
            if cc > abs(s):
                cc = abs(s)
                area = i * j
    print(area)

if __name__ == '__main__':
    main(2000000)
