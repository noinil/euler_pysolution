#!/bin/env python

def fibo(n):
    fiboseries = []
    a, b = 1, 2
    while a < n:
        a, b = b, a + b
        fiboseries.append(a)
    return fiboseries

if __name__ == "__main__":
    print(sum(i for i in fibo(4000000) if i%2==0))
