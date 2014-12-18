#!/usr/bin/env python3

def main():
    nnn = 1
    ddd = 1
    for denom in range(12, 100):
        for numer in range(11, denom):
            ds = set(str(denom))
            ns = set(str(numer))
            d = ds - ns
            n = ns - ds
            if len(d) == 2 or len(n) == 2 or len(d) == 0 or len(n) == 0:
                continue
            den1 = int(d.pop())
            num1 = int(n.pop())
            if denom == den1 * 10 and numer == num1 * 10:
                continue
            if denom == den1 * 11 and numer == num1 * 11:
                continue
            if numer * den1 == num1 * denom:
                print(numer, '/', denom, '=', num1, '/', den1)
                nnn, ddd = nnn * num1, ddd * den1
    print(nnn, '/', ddd)

if __name__ == '__main__':
    main()
