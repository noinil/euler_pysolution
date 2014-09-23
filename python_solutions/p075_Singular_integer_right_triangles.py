#!/usr/bin/env python

import math

def L(x, y):
    return 2 * x * (x + y)

def main(N):
    n = math.ceil(math.sqrt(N / 2))
    foldable_dict = {}
    for i in range(2, n):
        for j in range(1, i):
            print(i, j)
            l = L(i, j)
            if l > N:
                break
            x = i ** 2 - j ** 2
            y = 2 * i * j
            v = 0
            while True:
                v += 1
                w = v * l
                if w > N:
                    break
                if w in foldable_dict.keys():
                    if x <= y:
                        foldable_dict[w].add((x*v, y*v))
                    else:
                        foldable_dict[w].add((y*v, x*v))
                else:
                    if x <= y:
                        foldable_dict[w] = {(x*v, y*v)}
                    else:
                        foldable_dict[w] = {(y*v, x*v)}
    count = 0
    for j in foldable_dict.values():
        if len(j) == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
