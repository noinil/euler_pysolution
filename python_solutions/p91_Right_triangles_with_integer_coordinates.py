#!/usr/bin/env python

def is_right_triangle(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    c12 = x1 * x2 + y1 * y2
    c13 = x1 * dx + y1 * dy
    c23 = x2 * dx + y2 * dy
    if c12 * c13 * c23 == 0:
        return True
    else:
        return False

def main():
    count = 0
    for x1 in range(1, 51):
        for y1 in range(0, 51):
            for x2 in range(0, 51):
                for y2 in range(1, 51):
                    if x2 != 0 and y2 / x2 <= y1 / x1:
                        continue
                    if is_right_triangle(x1, y1, x2, y2):
                        count += 1
    print(count)

if __name__ == '__main__':
    main()
