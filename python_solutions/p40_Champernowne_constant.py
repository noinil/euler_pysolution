#!/usr/bin/env python

def main(N):
    digi = ''
    i = 1
    while True:
        digi = digi + str(i)
        if len(digi) >= N + 1:
            break
        i = i + 1
    print(int(digi[0]) * int(digi[9]) * int(digi[99]) * int(digi[999])\
          * int(digi[9999]) * int(digi[99999]) * int(digi[999999]))

if __name__ == '__main__':
    main(1000000)
