#!/bin/env python3

def digit_num(i):
    digi_str_0_ = {1 : 3, 2 : 3, 3 : 5, 4 : 4, 5 : 4,\
                   6 : 3, 7 : 5, 8 : 5, 9 : 4, 0 : 0}
    digi_str_1_ = {1 : 6, 2 : 6, 3 : 8, 4 : 8, 5 : 7,\
                   6 : 7, 7 : 9, 8 : 8, 9 : 8, 0 : 3}
    digi_str_2_ = {2 : 6, 3 : 6, 4 : 5, 5 : 5,\
                   6 : 5, 7 : 7, 8 : 6, 9 : 6}
    digi_str1__ = {1 : 13, 2 : 13, 3 : 15, 4 : 14, 5 : 14,\
                   6 : 13, 7 : 15, 8 : 15, 9 : 14, 0 : 0}
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    num = 0
    if i % 100 == 0:
        num = num + digi_str1__[a] - 3
    else:
        num = num + digi_str1__[a]
    if b == 1:
        num = num + digi_str_1_[c]
    elif b >= 2:
        num = num + digi_str_2_[b] + digi_str_0_[c]
    else:
        num = num + digi_str_0_[c]
    return num


if __name__ == "__main__":
    '''Answer: 21124'''

    N = 1000
    a = 0
    b = 0
    c = 0

    s = 0

    for i in range(1, N):
        s = s + digit_num(i)

    print(s + 11)
