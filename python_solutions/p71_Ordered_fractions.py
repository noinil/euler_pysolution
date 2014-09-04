#!/usr/bin/env python

def main(N):
    import fractions as fr
    c = 3/7
    close = 0
    cf = fr.Fraction(1, 7)
    for i in range(2, N + 1):
        t = c * i
        tf = fr.Fraction(int(t), i)
        t = int(t)/i
        if close < t < c:
            close = t
            cf = tf
            print(tf)


if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
