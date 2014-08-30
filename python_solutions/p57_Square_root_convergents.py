#!/usr/bin/env python

def main():
    import fractions
    s = 1
    count = 0
    for i in range(1, 1001):
        s = 1 + fractions.Fraction(1, 1+s)
        numer = s.numerator
        denom = s.denominator
        if len(str(numer)) > len(str(denom)):
            count = count + 1
    print(count)

if __name__ == '__main__':
    main()
