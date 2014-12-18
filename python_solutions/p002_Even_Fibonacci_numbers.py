#!/usr/bin/env python3

def fibo(n):
    fiboseries = []
    a, b = 1, 2
    while a < n:
        a, b = b, a + b
        fiboseries.append(a)
    return fiboseries

def main():
    print(sum(i for i in fibo(4000000) if i%2==0))

if __name__ == '__main__':
    main()
