#!/usr/bin/env python

def main():
    N = 10000000
    # set1 = {1}
    # set89 = {89}
    count = 0
    for i in range(2, N):
        print(i)
        # if i in set89:
        #     count += 1
        #     continue
        # if i in set1:
        #     continue
        # locset = {i}
        j = i
        while True:
            j = sum([int(a) * int(a) for a in str(j)])
            # if j in set89:
                # set89 = set89.union(locset)
                # break
            # if j in set1:
                # set1 = set1.union(locset)
                # break
            if j == 89:
                count += 1
                break
            elif j == 1:
                break
            # locset.add(j)
        # print(len(set1), len(set89))
    print(count)

if __name__ == '__main__':
    main()
