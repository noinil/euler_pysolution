#!/usr/bin/env python3

def main():
    import sympy
    N = 100000
    n_list = []
    for i in range(3, N):
        if i == sum([sympy.factorial(j) for j in str(i)[:]]):
            n_list.append(i)

    print(sum(n_list))

if __name__ == '__main__':
    main()
