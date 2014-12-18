#!/usr/bin/env python3

def palind_add(n):
    s = str(n)
    t = s[::-1]
    m = int(t)
    return m + n

def is_palind(n):
    s = str(n)
    t = s[::-1]
    if s == t:
        return True
    else:
        return False



def main():
    N = 10000
    count = 0
    for i in range(1, N):
        flag = 0
        m = i
        for c in range(0, 50):
            m = palind_add(m)
            if is_palind(m):
                break
        else:
            print(i)
            count = count + 1
    print(count)

if __name__ == '__main__':
    main()
