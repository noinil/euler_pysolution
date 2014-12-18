#!/usr/bin/env python3

def pandigital_list():
    import itertools
    funlist = []
    s = '0123456789'
    p = list(itertools.permutations(s))
    for i in p:
        if int(i[0]) == 0 or (i[5] != '5' and i[5] != '0') or int(i[3]) % 2 != 0:
            continue
        s = ''
        for j in i:
            s = s + j
        funlist.append(int(s))
    return funlist

def is_lucky_number(n):
    s = str(n)
    g = int(s[1:4])
    a = int(s[2:5])
    h = int(s[3:6])
    b = int(s[4:7])
    c = int(s[5:8])
    d = int(s[6:9])
    e = int(s[7:10])
    if g % 2 == 0 and a % 3 == 0 and b % 7 == 0 and c % 11 == 0 and d % 13 == 0\
       and h % 5 == 0 and e % 17 == 0:
        return True
    else:
        return False

def main():
    import sympy

    llist = []
    plist = pandigital_list()
    for j in plist[:]:
        if is_lucky_number(j):
            llist.append(j)
    print(sum(llist))

if __name__ == '__main__':
    main()
