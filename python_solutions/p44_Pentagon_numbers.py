#!/usr/bin/env python

def is_pentagon(n):
    import math
    for i in range(1, int(math.sqrt(n))):
        if n == i * ( 3 * i - 1) // 2:
            return True
    else:
        return False


def main():
    i = 10000
    while True:
        bi = i * ( 3 * i - 1) // 2
        for j in range(2, int((bi - 1) // 3) + 1):
            aj = j * ( 3 * j - 1) // 2
            if is_pentagon(aj + bi) and is_pentagon(aj * 2+ bi):
                print(bi)
                return
        else:
            print(i, bi)
            i = i + 1

if __name__ == '__main__':
    main()
