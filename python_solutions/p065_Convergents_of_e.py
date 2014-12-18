#!/usr/bin/env python3

def main(N):
    a0, a1 = 2, 1
    h0, h1 = 2, 3
    k0, k1 = 1, 1
    for i in range(2, N):
        if i % 3 == 2:
            a = 2 * ( i // 3 + 1)
        else:
            a = 1
        h1, h0 = a * h1 + h0, h1
        k1, k0 = a * k1 + k0, k1
    print(h1, k1)
    print(sum([int(i) for i in str(h1)]))


if __name__ == '__main__':
    main(100)
