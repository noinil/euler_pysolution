#!/usr/bin/env python

def main():
    i = 0
    count = 0
    while True:
        i = i + 1
        for n in range(1, 10):
            if n ** i >= 10 ** (i - 1):
                count = count + (10 - n)
                break
        else:
            break
    print(count)

if __name__ == '__main__':
    main()
