#!/usr/bin/env python

def main():
    import sympy as sp
    i = 2
    while True:
        i = i + 1
        if len(sp.primefactors(i)) == 4:
            i = i + 1
            if len(sp.primefactors(i)) == 4:
                i = i + 1
                if len(sp.primefactors(i)) == 4:
                    i = i + 1
                    if len(sp.primefactors(i)) == 4:
                        print(i - 3)
                        return

if __name__ == '__main__':
    main()
