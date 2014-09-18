#!/usr/bin/env python

def main():
    # read in the data
    mat = []
    lm = []
    with open("../data/p83_matrix.txt", 'r') as fmat:
        for line in fmat:
            for i in line.split(','):
                lm.append(int(i))
            mat.append(lm[:])
            lm.clear()
    L = len(mat)

    # two lists
    l_done = {(0, 0) : mat[0][0]}
    l_todo = [(0, 0)]

    # -------------------- calculating loop --------------------
    while True:
        # checking todo list
        #          f3
        #          |
        #  f1 -- coor -- f2
        #          |
        #          f4
        #
        min_v = -1
        nearest_coor = (0, 0)
        print(l_todo)
        for coor in l_todo[:]:
            x, y = coor[0], coor[1]
            f1, f2, f3, f4 = 0, 0, 0, 0
            if x == 0:
                f1 = 1
            else:
                coor1 = (x - 1, y)
                if coor1 in l_done:
                    f1 = 1
                else:
                    dis_v = l_done[coor] + mat[x - 1][y]
                    if min_v == -1 or min_v > dis_v:
                        min_v, nearest_coor = dis_v, coor1
            if x == L - 1:
                f2 = 1
            else:
                coor1 = (x + 1, y)
                if coor1 in l_done:
                    f2 = 1
                else:
                    dis_v = l_done[coor] + mat[x + 1][y]
                    if min_v == -1 or min_v > dis_v:
                        min_v, nearest_coor = dis_v, coor1
            if y == 0:
                f3 = 1
            else:
                coor1 = (x, y - 1)
                if coor1 in l_done:
                    f3 = 1
                else:
                    dis_v = l_done[coor] + mat[x][y - 1]
                    if min_v == -1 or min_v > dis_v:
                        min_v, nearest_coor = dis_v, coor1
            if y == L - 1:
                f4 = 1
            else:
                coor1 = (x, y + 1)
                if coor1 in l_done:
                    f4 = 1
                else:
                    dis_v = l_done[coor] + mat[x][y + 1]
                    if min_v == -1 or min_v >= dis_v:
                        min_v, nearest_coor = dis_v, coor1
            if f1 * f2 * f3 * f4 == 1:
                # print(coor, "removed!")
                l_todo.remove(coor)

        # set the nearest neighbor
        l_todo.append(nearest_coor)
        l_done[nearest_coor] = min_v
        print(nearest_coor, mat[nearest_coor[0]][nearest_coor[1]], min_v)
        if nearest_coor == (L-1, L-1):
            print(nearest_coor, min_v)
            break

if __name__ == '__main__':
    main()
