#!/usr/bin/env python

def main(N):
    perimeter_sum = 0
    for a in range(1, round(((N + 1) / 6) ** 0.5)):
        for b in range(a - 1, 0, -2):
            i = a * a - b * b
            j = 2 * a * b
            k = a * a + b * b
            if abs(i * 2 - k) == 1:
                perimeter_sum += 2 * (i + k) if 2 * (i + k) < N else 0
            if abs(j * 2 - k) == 1:
                perimeter_sum += 2 * (j + k) if 2 * (j + k) < N else 0
    print("perimeter_sum =", perimeter_sum)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
