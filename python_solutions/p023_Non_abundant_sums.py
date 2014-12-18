#!/bin/env python3

import p21_Amicable_numbers as p21

def main():
    N = 28123

    abundant_list = [i for i in range(4, N+1) if  p21.fac_sum(i) > i]
    print(" Abundant list generated.")

    lucky_list = [i + j for i in abundant_list for j in abundant_list if i + j < N]
    lucky_set = set(lucky_list)
    total_set = {i for i in range(1, N)}

    unlucky_set = total_set - lucky_set

    print(unlucky_set)
    # print(sum(lucky_list))
    print(sum(unlucky_set))

if __name__ == '__main__':
    main()
