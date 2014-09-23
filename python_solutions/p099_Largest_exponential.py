#!/usr/bin/env python

import math

def main():
    maxlog, line_number, i = 0, 0, 0
    with open("../data/p99_base_exp.txt", "r") as fin:
        for line in fin:
            i += 1
            a, b = int(line.split(',')[0]), int(line.split(',')[1])
            m = b * math.log(a)
            if maxlog == 0 or maxlog < m:
                maxlog, ln = m, i
    print(maxlog, ln)

if __name__ == '__main__':
    main()
