#!/usr/bin/env python3

def main():
    roman_mat = []
    with open("../data/p89_roman.txt", "r") as fin:
        for line in fin:
            roman_mat.append(line.split()[0])

    count = 0
    for i in roman_mat[:]:
        s = i
        n = 0
        if 'IV' in s:
            s = s[:s.index('IV')] + s[s.index('IV')+2:]
            n += 4
        if 'IX' in s:
            s = s[:s.index('IX')] + s[s.index('IX')+2:]
            n += 9
        if 'XL' in s:
            s = s[:s.index('XL')] + s[s.index('XL')+2:]
            n += 40
        if 'XC' in s:
            s = s[:s.index('XC')] + s[s.index('XC')+2:]
            n += 90
        if 'CD' in s:
            s = s[:s.index('CD')] + s[s.index('CD')+2:]
            n += 400
        if 'CM' in s:
            s = s[:s.index('CM')] + s[s.index('CM')+2:]
            n += 900
        for c in s:
            if c == 'M':
                n += 1000
            elif c == 'D':
                n += 500
            elif c == 'C':
                n += 100
            elif c == 'L':
                n += 50
            elif c == 'X':
                n += 10
            elif c == 'V':
                n += 5
            elif c == 'I':
                n += 1
            else:
                print('error!')
                break
        # print(i, " = ", n)
        sn = str(n)
        nn = 0
        for c in sn:
            cn = int(c)
            if nn == 0 and len(sn) == 4:
                nn += cn
                continue
            if cn <= 3:
                nn += cn
            elif cn == 5:
                nn += 1
            elif cn == 4 or cn == 9:
                nn += 2
            elif cn <= 8:
                nn += cn - 4
        print(i, " = ", n, "  len = ", nn, len(i))
        count += len(i) - nn

    print("total reduction:", count)

if __name__ == '__main__':
    main()
