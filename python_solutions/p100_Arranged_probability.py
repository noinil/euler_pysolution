#!/usr/bin/env python

def main(N):
    u, v = N**0.5, 1
    while True:
        u, v = u + 1, 0
        t1, t2 = round((2 * u * u + 1)**0.5), round((2 * u * u - 1)**0.5)
        if t1 * t1 == 2 * u * u + 1:
            v = t1 - u
        if t2 * t2 == 2 * u * u - 1:
            v = t2 - u
        if v != 0:
            print("m =", u**2 - v**2 + 1, "n =", (u**2+v**2+1)//2)
            if u**2 - v**2 > N:
                return 0

if __name__ == '__main__':
    import time
    tb = time.time()
    main(10**12)
    te = time.time()
    print("time:", te-tb)
