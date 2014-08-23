#!/usr/bin/env python

def main():
    way = 1
    i, j, k, l, m, n, o = 0, 0, 0, 0, 0, 0, 0
    for i in range(0, 3):
        total = 100 * i
        if total == 200:
            print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
            way = way + 1
            continue
        if total > 200:
            continue
        for j in range(0, 5):
            total = 100 * i + 50 * j
            if total == 200:
                print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
                way = way + 1
                break
            if total > 200:
                break
            for k in range(0, 11):
                total = 100 * i + 50 * j + 20 * k
                if total == 200:
                    print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
                    way = way + 1
                    break
                if total > 200:
                    break
                for l in range(0, 21):
                    total = 100 * i + 50 * j + 20 * k + 10 * l
                    if total == 200:
                        print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
                        way = way + 1
                        break
                    if total > 200:
                        break
                    for m in range(0, 41):
                        total = 100 * i + 50 * j + 20 * k + 10 * l + 5 * m
                        if total == 200:
                            print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
                            way = way + 1
                            break
                        if total > 200:
                            break
                        for n in range(0, 101):
                            total = 100 * i + 50 * j + 20 * k + 10 * l + 5 * m + 2 * n
                            if total == 200:
                                print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
                                way = way + 1
                                break
                            if total > 200:
                                break
                            for o in range(0, 201):
                                total = 100 * i + 50 * j + 20 * k + 10 * l + 5 * m + 2 * n + o
                                if total == 200:
                                    print("100 *", i, "+ 50 *", j, "+ 20 *", k, "+ 10 *", l, "+ 5 *", m, "+ 2 *", n, "+", o)
                                    way = way + 1
                                    break
                                if total > 200:
                                    break
    print(way)

if __name__ == '__main__':
    main()
