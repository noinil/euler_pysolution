#!/usr/bin/env python

def digi_sum(n):
    s = str(n)
    return sum([int(i) for i in s[:]])

def main():
    rub = 0
    for i in range(2,100):
        for j in range(2, 100):
            s = digi_sum(i**j)
            if s > rub:
                rub = s
    print(rub)

if __name__ == '__main__':
    main()
