#!/usr/bin/env python3

def main():
    mat = []
    lm = []
    with open("../data/p82_matrix.txt", 'r') as fmat:
    # with open("test.txt", 'r') as fmat:
        for line in fmat:
            for i in line.split(','):
                lm.append(int(i))
            mat.append(lm[:])
            lm.clear()
    L = len(mat)

    a = [m[0] for m in mat]
    print(a)
    b = []
    c = []
    for i in range(1, L):
        b = [m[i] for m in mat]
        print(b)
        for j in range(0, L):
            t = 0
            for k in range(0, L):
                s = a[k]
                s += sum(b[k:j]) if k <= j else sum(b[j + 1 : k + 1])
                if k == 0 or s < t:
                    t = s
            t += b[j]
            c.append(t)
        print("c = ", c)
        a = c[:]
        c.clear()
    print(min(a))
if __name__ == '__main__':
    main()
