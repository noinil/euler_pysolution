#!/usr/bin/env python

def main():
    from operator import xor
    coded_txt = []
    origin_txt = ''
    with open("../data/p59_cipher.txt", 'r') as f:
        line = f.readline()
        for s in line.split(','):
            coded_txt.append(int(s))
    print("coded text has", len(coded_txt), "chars!")
    print(coded_txt)
    for x in range(0, 128):
        c = xor(x, coded_txt[0])
        if c > 122 or c < 31:
            continue
        for y in range(0, 128):
            c = xor(y, coded_txt[1])
            if c > 122 or c < 31:
                continue
            for z in range(0, 128):
                c = xor(z, coded_txt[2])
                if c > 122 or c < 31:
                    continue

                key = [x, y, z]
                # print("key = ", key)
                for i in range(0, len(coded_txt)):
                    j = i % 3
                    c = xor(key[j], coded_txt[i])
                    origin_txt = origin_txt + chr(c)
                    if c < 31 or c > 122:
                        break
                else:
                    print(origin_txt)
                    print(key)
                    ascsum = sum([ord(i) for i in origin_txt[:]])
                    print("the sum of origin text is:", ascsum)
                    # return
                # print(origin_txt)
                origin_txt = ''

if __name__ == '__main__':
    main()
