#!/bin/env python3

N = 100

s = sum([i*j for i in range(1, N+1) for j in range(1, N+1) if i != j])
print(s)
