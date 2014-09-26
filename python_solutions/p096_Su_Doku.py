#!/usr/bin/env python

def solve_sudoku(s):
    bin_full = 2 ** 9 - 1                    # 0b111111111
    bin_list = [2 ** i for i in range(0, 9)] # 0b000000001 ~ 0b100000000
    bin2dec  = {bin_list[i] : i + 1 for i in range(0, 9)}

    sudoku = s[:]
    todoku = [[bin_full for i in range(0, 9)] for j in range(0, 9)]
    n_blank = 0                 # number of blanks

    # ------------ find blanks and eliminate possible numbers ------------------
    def _eliminate():
        for i in range(0, 9):
            for j in range(0, 9):
                if sudoku[i][j] != 0:
                    todoku[i][j] = bin_list[sudoku[i][j] - 1]
                    flt = bin_full ^ todoku[i][j]
                    for k in range(0, 9):
                        if sudoku[i][k] == 0:             # eliminates row -----
                            todoku[i][k] = todoku[i][k] & flt
                        if sudoku[k][j] == 0:             # eliminates column --
                            todoku[k][j] = todoku[k][j] & flt
                    m, n = i // 3, j // 3
                    for x in range(0, 3):                 # eliminates box -----
                        for y in range(0, 3):
                            u, v = m * 3 + x, n * 3 + y
                            if sudoku[u][v] == 0:
                                todoku[u][v] = todoku[u][v] & flt
    # ---------- check every blank to fill in only possible numbers ------------
    def _unique():
        checkcount = 0
        nonlocal n_blank
        n_blank = 81
        for i in range(0, 9):
            for j in range(0, 9):
                if sudoku[i][j] != 0:
                    n_blank -= 1
                    continue
                t = todoku[i][j]
                if t in bin_list:
                    sudoku[i][j] = bin2dec[t]
                    checkcount += 1
                    n_blank -= 1
        return checkcount
    # ---------- check each line for candidate numbers only appear once --------
    def _orphan():
        for i in range(0, 9):   # check rows ----------
            todo_keys = {i : [] for i in range(1, 10)}
            for j in range(0, 9):
                if sudoku[i][j] != 0:
                    continue
                t = todoku[i][j]
                for e in bin_list:
                    ke = t & e
                    if ke != 0:
                        todo_keys[bin2dec[ke]].append(j)
            for k, l in todo_keys.items():
                if len(l) == 1:
                    idx = l[0]
                    sudoku[i][idx] = k
                    _eliminate()
        for j in range(0, 9):   # check columns ----------
            todo_keys = {i : [] for i in range(1, 10)}
            for i in range(0, 9):
                if sudoku[i][j] != 0:
                    continue
                t = todoku[i][j]
                for e in bin_list:
                    ke = t & e
                    if ke != 0:
                        todo_keys[bin2dec[ke]].append(i)
            for k, l in todo_keys.items():
                if len(l) == 1:
                    idx = l[0]
                    sudoku[idx][j] = k
                    _eliminate()
        for i in range(0, 3):   # check each 3*3 box ----------
            for j in range(0, 3):
                todo_keys = {i : [] for i in range(1, 10)}
                for x in range(0, 3):
                    for y in range(0, 3):
                        u, v = i * 3 + x, j * 3 + y
                        if sudoku[u][v] != 0:
                            continue
                        t = todoku[u][v]
                        for e in bin_list:
                            ke = t & e
                            if ke != 0:
                                todo_keys[bin2dec[ke]].append((u, v))
                for k, l in todo_keys.items():
                    if len(l) == 1:
                        idx, idy = l[0][0], l[0][1]
                        sudoku[idx][idy] = k
                        _eliminate()

    # -------------------- Check -----------------------------------------------
    def _check():
        for i in range(0, 9):
            check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -- check row
            for j in range(0, 9):
                if sudoku[i][j] not in check_list:
                    print("row", i, "element", i, j, sudoku[i][j], "out of list!")
                    return False
                else:
                    check_list.remove(sudoku[i][j])
            if len(check_list) != 0:
                print("row:", i, "conflict!")
                return False
            check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -- check column
            for j in range(0, 9):
                if sudoku[j][i] not in check_list:
                    print("column", i, "element", j, i, sudoku[j][i], "out of list!")
                    return False
                else:
                    check_list.remove(sudoku[j][i])
            if len(check_list) != 0:
                print("column:", i, "conflict!")
                return False
        for i in range(0, 3):
            for j in range(0, 3):
                check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -- check box
                for x in range(0, 3):
                    for y in range(0, 3):
                        u, v = i * 3 + x, j * 3 + y
                        if sudoku[u][v] not in check_list:
                            print("box", i, ":", j, "element", u, v, sudoku[i][j], "out of list!")
                            return False
                        else:
                            check_list.remove(sudoku[u][v])
                if len(check_list) != 0:
                    print("box:", i, j, "conflict!")
                    return False
        return True

    def _minor_check():
        for i in range(0, 9):
            check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -- check row
            for j in range(0, 9):
                if sudoku[i][j] == 0:
                    continue
                elif sudoku[i][j] not in check_list:
                    return False
                else:
                    check_list.remove(sudoku[i][j])
            check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -- check column
            for j in range(0, 9):
                if sudoku[j][i] == 0:
                    continue
                elif sudoku[j][i] not in check_list:
                    return False
                else:
                    check_list.remove(sudoku[j][i])
        for i in range(0, 3):
            for j in range(0, 3):
                check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -- check box
                for x in range(0, 3):
                    for y in range(0, 3):
                        u, v = i * 3 + x, j * 3 + y
                        if sudoku[u][v] == 0:
                            continue
                        elif sudoku[u][v] not in check_list:
                            return False
                        else:
                            check_list.remove(sudoku[u][v])
        return True

    # -------------------- Output functions --------------------
    def output_sudoku():
        for row in sudoku:
            print(row)
        print(" ------------------------------")
    def output_todoku():
        for row in todoku:
            print(row)
        print(" ------------------------------")

    while True:
        _eliminate()
        if _unique() == 0:
            _orphan()
            if _unique() == 0:
                break

    if n_blank == 0 and _check():
        print("solved!")
        output_sudoku()
        print(" ============================== ")
        return sudoku

    # ==================== stacking methods ====================
    todoku = [[bin_full for i in range(0, 9)] for j in range(0, 9)]
    _eliminate()
    index_todoku = []
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                s = todoku[i][j]
                possible_nums = []
                for t in bin_list:
                    if t & s == t:
                        possible_nums.append(bin2dec[t])
                index_todoku.append([i, j, possible_nums])
    sutacku = [sudoku[:]]
    intacku = []
    il = 0
    while True:
        if len(intacku) == il:
            l = index_todoku[il]
            i, j = l[0], l[1]
            try_list = l[2][:]
            test_s = try_list.pop()
            intacku.append([i, j, try_list])
        else:
            i, j = intacku[il][0], intacku[il][1]
            if len(intacku[il][2]) == 0:
                if il == 0:
                    print(" No Solution!")
                    print(" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
                    return sudoku
                il -= 1
                sudoku = sutacku.pop()
                intacku.pop()
                continue
            test_s = intacku[il][2].pop()
        sudoku[i][j] = test_s
        if _minor_check():
            s = []
            for i in sudoku:
                line_tmp = []
                for j in i:
                    line_tmp.append(j)
                s.append(line_tmp)
            sutacku.append(s)
            il += 1
            if il >= len(index_todoku) and _check():
                print("Solved!")
                output_sudoku()
                print(" ==============================")
                return sudoku
    print("UNSOLVED!", n_blank, "blanks left!")
    print(" ============================== ")
    return sudoku

def main():
    mat_sudoku = []
    with open("../data/p096_sudoku.txt", "r") as fin:
        loc_mat = []
        for line in fin:
            if line.split()[0] == "Grid":
                if len(loc_mat) == 0:
                    continue
                mat_sudoku.append(loc_mat[:])
                loc_mat.clear()
                continue
            loc_line = [int(i) for i in line.split()[0]]
            loc_mat.append(loc_line[:])
    mat_sudoku.append(loc_mat[:])

    count = 0
    for sudoku in mat_sudoku[:]:
        s = solve_sudoku(sudoku)
        a, b, c = s[0][0], s[0][1], s[0][2]
        count += a * 100 + b * 10 + c

    print(count)

if __name__ == '__main__':
    main()
