#!/usr/bin/env python3

import itertools

def good_dices(a, b):
    t = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
    for i in a:
        for j in b:
            sa, sb = str(i), str(j)
            sab, sba = sa + sb, sb + sa
            if sab in t:
                t.remove(sab)
            if sba in t:
                t.remove(sba)
    if len(t) == 0:
        return True
    else:
        return False

def main():
    rep = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    count = 0
    dices = list(itertools.combinations(rep, 6))
    good_set = set()
    for i in dices:
        li = list(i)
        if 6 in li and 9 not in li:
            li.append(9)
        if 9 in li and 6 not in li:
            li.append(6)
        for j in dices[dices.index(i) + 1:]:
            if j == i:
                continue
            lj = list(j)
            if 6 in lj and 9 not in lj:
                lj.append(9)
            if 9 in lj and 6 not in lj:
                lj.append(6)
            if good_dices(li, lj):
                print(i, j)
                count += 1
    print(count)

if __name__ == '__main__':
    main()
