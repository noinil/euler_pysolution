#!/usr/bin/env python

def main():
    triangle = []
    with open('../data/p67_triangle.txt', 'r') as f:
        locang = []
        for lines in f:
            for i in lines.split():
                locang.append(int(i))
            triangle.append(locang[:])
            locang.clear()

    leng = len(triangle)
    for i in range(1, leng):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j], triangle[i][j] + triangle[i-1][j-1])
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]

    print(triangle[-1])
    print(max(triangle[-1]))

if __name__ == '__main__':
    main()
