#!/usr/bin/env python

def recurring_len(n):
    rem = []
    a = 1
    count = 0
    while True:
        a = a * 10 % n
        if a in rem:
            break
        rem.append(a)
        count = count + 1
    return count

def main(n):
    max_rec_len = 0
    max_num = 0
    for i in range(2, n + 1):
        m = recurring_len(i)
        if max_rec_len < m:
            max_rec_len = m
            max_num = i
    print(max_num, "has the recurring length of", max_rec_len)

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])

    main(N)
