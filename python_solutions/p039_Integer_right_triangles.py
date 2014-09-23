#!/usr/bin/env python

def main(n):
    import math
    best = 0
    count = 0
    for i in range(12, n+1, 2):
        m = i // 2
        c = 0
        for a in range(int(math.sqrt(i)/2), m):
            if m % a == 0:
                c = c + 1
        if count < c:
            count = c
            best = i
    print(best)

if __name__ == '__main__':
    main(1000)
