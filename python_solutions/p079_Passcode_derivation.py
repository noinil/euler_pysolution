#!/usr/bin/env python

def main():
    a = []
    pscd = []
    with open("../data/p79_keylog.txt", "r") as f:
        for line in f:
            s = line.split()[0]
            ll = [int(i) for i in list(s)]
            pscd.append(ll)
    for l in pscd:
        for x in l:
            if x not in a:
                a.append(x)
        x1, x2, x3 = l[0], l[1], l[2]
        if a.index(x1) > a.index(x2):
            a.remove(x1)
            a.insert(a.index(x2), x1)
        if a.index(x2) > a.index(x3):
            a.remove(x2)
            a.insert(a.index(x3), x2)
        print(a)
    print(a)

if __name__ == '__main__':
    main()
