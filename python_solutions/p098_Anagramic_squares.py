#!/usr/bin/env python3

from itertools import permutations as pm

def is_sqr(n):
    i = round(n**0.5)
    if i ** 2 == n:
        return True
    else:
        return False

def main():
    words = []
    with open("../data/p98_words.txt", "r") as fin:
        for lines in fin:
            for i in lines.split(','):
                if i != i[::-1]:
                    words.append(i[1:-1])

    vals = []
    anagramic_pairs = []
    c_vals = []
    for i in words:
        t = 0
        for c in i[:]:
            t += 10**(ord(c) - ord('A'))
        if t in vals:
            if t in c_vals:
                anagramic_pairs.append((words[vals.index(t, vals.index(t)+1)], i))
            c_vals.append(t)
            anagramic_pairs.append((words[vals.index(t)], i))
        vals.append(t)

    sqr_list = [i**2 for i in range(0, 4*10**4) if i**2 < 10**9]
    digi_list = [i for i in range(0, 10)]

    for i in anagramic_pairs:
        worda, wordb = i[0], i[1]
        chl = []
        for c in worda:
            if c not in chl:
                chl.append(c)
        n = len(chl)
        print(worda, wordb, n)
        pmiter = pm(digi_list, n)
        for j in pmiter:
            wa, wb = worda, wordb
            for k in range(0, n):
                wa = wa.replace(chl[k], str(j[k]))
                wb = wb.replace(chl[k], str(j[k]))
            if wa[0] == '0' or wb[0] == '0':
                continue
            va, vb = int(wa), int(wb)
            # if va in sqr_list and vb in sqr_list:
            if is_sqr(va) and is_sqr(vb):
                print(worda, wordb, va, vb)

if __name__ == '__main__':
    main()
