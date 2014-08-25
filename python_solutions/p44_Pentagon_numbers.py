#!/usr/bin/env python

def is_pentagon(n):
    import math
    i = int(math.sqrt(24 * n + 1))
    if i * i == 24 * n + 1 and i % 6 == 5:
        return True
    else:
        return False


def main():
    i = 1
    while True:
        bi = i * ( 3 * i - 1) // 2
        for j in range(i, int((bi - 1) // 3) + 1):
            aj = j * ( 3 * j - 1) // 2
            c = aj + bi
            d = aj * 2 + bi
            e = aj + bi * 2
            if is_pentagon(c):
                print("P", i, "P", j)
                if is_pentagon(d):
                    print(bi)
                    return
                if is_pentagon(e):
                    print(aj)
                    return
        i = i + 1

if __name__ == '__main__':
    main()
