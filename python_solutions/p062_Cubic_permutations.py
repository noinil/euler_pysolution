#!/usr/bin/env python3

def cube_digi_score(n):
    s = str(n*n*n)
    return sum([10**int(i) for i in s[:]])

def main():
    score_list = [cube_digi_score(i) for i in range(1, 10000)]
    printed_numbers = set()
    for j in score_list:
        if j in printed_numbers:
            continue
        if score_list.count(j) == 5:
            a1 = score_list.index(j)+1
            a2 = score_list.index(j, a1,) + 1
            a3 = score_list.index(j, a2,) + 1
            printed_numbers.add(j)
            print(a1, a2, a3)
            print(a1*a1*a1)

if __name__ == '__main__':
    main()
