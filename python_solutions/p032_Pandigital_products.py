#!/usr/bin/env python3

def main():
    product_set = set()
    for i in range(2, 99):
        for j in range(123, 9877):
            mul = i * j
            if mul >= 10000:
                break
            if mul <= 999:
                continue
            digi_st = str(i) + str(j) + str(mul)
            if len(set(digi_st)) == 9 and '0' not in set(digi_st):
                print(i, "x", j, "=", mul)
                product_set.add(mul)

    print(sum(product_set))
    print(product_set)

if __name__ == '__main__':
    main()
