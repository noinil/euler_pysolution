#!/usr/bin/env python3

def area_triangle_2(coor1, coor2, coor3):
    """Calculate area of triangle from the coordinates of vertexes.
    Keyword Arguments:
    coor1 -- coordinate of vertex 1
    coor2 -- coordinate of vertex 2
    coor3 -- coordinate of vertex 3
    """
    x1, y1 = coor1
    x2, y2 = coor2
    x3, y3 = coor3
    return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)

def main():
    count = 0
    with open('../data/p102_triangles.txt', 'r') as fin:
        for lines in fin:
            coors = lines.split(',')
            c = [int(i) for i in coors]
            area0 = area_triangle_2((c[0], c[1]), (c[2], c[3]), (c[4], c[5]))
            area1 = area_triangle_2((c[0], c[1]), (c[2], c[3]), (0, 0))
            area2 = area_triangle_2((c[0], c[1]), (0, 0), (c[4], c[5]))
            area3 = area_triangle_2((0, 0), (c[2], c[3]), (c[4], c[5]))
            if area0 == area1 + area2 + area3:
                print("IN")
                count += 1
            else:
                print("OUT")
    print(count)

if __name__ == '__main__':
    main()
