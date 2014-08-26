#!/usr/bin/env python

import p37_Truncatable_primes as p37

def main(n):
    import sympy as sp
    for i in sp.primerange(100000, 1000000):
        digi_last = i % 10
        s = str(i//10)
        # if len(set(s)) > 3:
        #     continue
        for c in range(0, 2):
            if s.count(str(c)) == 3:
                count = 0
                local_list = []
                for d in range(c, 10):
                    new_s = s.replace(str(c), str(d))
                    new_digi = int(new_s) * 10 + digi_last
                    if p37.is_prime(new_digi):
                        count = count + 1
                        local_list.append(new_digi)
                        if count == n:
                            print("the lucky one:", i)
                            print(local_list)
                            return
                print(local_list)
            if s.count(str(c)) == 4:
                count = 0       # Replace the last one
                local_list = []
                for d in range(c, 10):
                    new_s = s.replace(str(c), str(d), 3)
                    new_digi = int(new_s) * 10 + digi_last
                    if p37.is_prime(new_digi):
                        count = count + 1
                        local_list.append(new_digi)
                        if count == n:
                            print("the lucky one:", i)
                            print(local_list)
                            return
                print(local_list)
                count = 0       # Replace the second one
                local_list = []
                for d in range(c, 10):
                    new_s = s.replace(str(c), str(d), 1)
                    new_s = new_s.replace(str(c), 'a', 1)
                    new_s = new_s.replace(str(c), str(d), 2)
                    new_s = new_s.replace('a', str(c), 1)
                    new_digi = int(new_s) * 10 + digi_last
                    if p37.is_prime(new_digi):
                        count = count + 1
                        local_list.append(new_digi)
                        if count == n:
                            print("the lucky one:", i)
                            print(local_list)
                            return
                print(local_list)
                count = 0       # Replace the third one
                local_list = []
                for d in range(c, 10):
                    new_s = s.replace(str(c), str(d), 2)
                    new_s = new_s.replace(str(c), 'a', 1)
                    new_s = new_s.replace(str(c), str(d), 1)
                    new_s = new_s.replace('a', str(c), 1)
                    new_digi = int(new_s) * 10 + digi_last
                    if p37.is_prime(new_digi):
                        count = count + 1
                        local_list.append(new_digi)
                        if count == n:
                            print("the lucky one:", i)
                            print(local_list)
                            return
                print(local_list)
                count = 0       # Replace the third one
                local_list = []
                for d in range(c, 10):
                    new_s = s.replace(str(c), 'a', 1)
                    new_s = new_s.replace(str(c), str(d), 3)
                    new_s = new_s.replace('a', str(c), 1)
                    new_digi = int(new_s) * 10 + digi_last
                    if p37.is_prime(new_digi):
                        count = count + 1
                        local_list.append(new_digi)
                        if count == n:
                            print("the lucky one:", i)
                            print(local_list)
                            return
                print(local_list)
        else:
            continue

if __name__ == '__main__':
    main(8)
