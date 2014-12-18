#!/bin/env python3

y = 1900
m = 1
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
d = 2
dd = 0

count = 0

for y in range(1901, 2001):
    if y % 4 == 0 and y != 2000:
        days[2] = 29
    else:
        days[2] = 28
    for m in range(1, 13):
        count = count + 1 if d == 0 else count
        d = (d + days[m]) % 7

print(count)
