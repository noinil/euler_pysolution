#!/usr/bin/env python

def pandigital(n):
    s_list = ''
    for i in range(1, 10):
        s_list = s_list + str(i * n)
        if len(s_list) > 9 or '0' in s_list:
            break
        if len(s_list) == 9 and len(set(s_list)) == 9:
            print(n, s_list)
            return int(s_list)
    return 0

def main():
    best = 0
    for i in range(1, 10000):
        m = pandigital(i)
        if m > best:
            best = m

    print(best)

if __name__ == '__main__':
    main()
