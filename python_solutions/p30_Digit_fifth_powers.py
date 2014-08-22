#!/usr/bin/env python

def main():
    total = 0
    N = 9999999 + 1
    for i in range(11, N):
        if i == sum([int(x)**5 for x in str(i)[:]]):
            print(i)
            total = total + i
    print(total)

if __name__ == '__main__':
    main()
