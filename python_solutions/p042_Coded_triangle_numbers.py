#!/usr/bin/env python

def alpha_value(s):
    return sum([ord(i) - ord('A') + 1 for i in s])

def main():
    triangle_list = [i * (i + 1) // 2 for i in range(1, 100)]
    with open('../data/p42_words.txt', 'r') as f:
        str = f.readlines()[0]
        quoted_names = str.split(sep = ',')
        names = [i[1:-1] for i in quoted_names]

    count = 0
    for i in names:
        if alpha_value(i) in triangle_list:
            count = count + 1

    print(count)

if __name__ == '__main__':
    main()
