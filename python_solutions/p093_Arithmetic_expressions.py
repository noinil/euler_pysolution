#!/usr/bin/env python3

import itertools

def main():
    ql = itertools.combinations([i for i in range(0, 10)], 4)
    fa = lambda x, y: x + y
    fb = lambda x, y: x - y
    fc = lambda x, y: x * y
    fd = lambda x, y: x / y
    fe = lambda x, y: y - x
    ff = lambda x, y: y / x
    flist = [fa, fb, fc, fd, fe, ff]

    best = 0
    best_l = ()
    for comb in ql:
        ans_list = set()
        ans = 0
        for i in itertools.permutations(comb, 4):
            for j in flist:
                for k in flist:
                    for l in flist:
                        try:
                            ans = j(k(l(i[0], i[1]), i[2]), i[3]) * 1.0
                        except ZeroDivisionError:
                            continue
                        if ans.is_integer() and ans > 0:
                            ans_list.add(int(ans))
        test = 1
        while True:
            if test not in ans_list:
                break
            test += 1
        test -= 1
        print(comb, len(ans_list), test)
        ans_list.clear()
        if best == 0 or best < test:
            best = test
            best_l = comb
    print(best, best_l)

if __name__ == '__main__':
    main()
