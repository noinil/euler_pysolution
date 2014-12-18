#!/usr/bin/env python3

def main():
    power_list = set()
    for i in range(2, 101):
        for j in range(2, 101):
            power_list.add(i**j)

    print(len(power_list))

if __name__ == '__main__':
    main()
