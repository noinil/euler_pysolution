#!/usr/bin/env python3

import random

def main(N):
    # -------------------- Generating the rooms --------------------
    room = [0 for i in range(0, 40)]

    # -------------------- Generating the cards --------------------
    cc_card = [i for i in range(1, 17)]
    ch_card = [i for i in range(1, 17)]
    random.shuffle(cc_card)
    random.shuffle(ch_card)

    def community_chest(x):
        card0 = cc_card.pop()
        cc_card.insert(0, card0)
        if card0 == 1:
            return 0
        elif card0 == 2:
            return 10
        else:
            return x

    def c_hance(x):
        card = ch_card.pop()
        ch_card.insert(0, card)
        if card == 1:
            return 0
        elif card == 2:
            return 10
        elif card == 3:
            return 11
        elif card == 4:
            return 24
        elif card == 5:
            return 39
        elif card == 6:
            return 5
        elif card == 7 or card == 8:
            if x == 7:
                return 15
            elif x == 22:
                return 25
            else:
                return 5
        elif card == 9:
            if x == 7 or x == 36:
                return 12
            elif x == 22:
                return 28
        elif card == 10:
            if x == 36:
                return community_chest(33)
                # return 33
            else:
                return x - 3
        else:
            return x

    # Looping!
    x = 0
    gg = 1000000

    df1 = 0
    df2 = 0
    df3 = 0
    for i in range(0, gg):
        # DICE!
        dice1 = random.randint(1, N)
        dice2 = random.randint(1, N)

        # check 3 doubles
        df1, df2 = df2, df3
        if dice1 == dice2:
            df3 = 1
        else:
            df3 = 0
        if df1 * df2 * df3 == 1:
            x = 10
            room[10] += 1
            continue
        x += (dice1 + dice2)
        if x > 39:
            x -= 40
        # ---------- G2J ----------
        if x == 30:
            x = 10
            room[10] += 1
            continue
        elif x == 2 or x == 17 or x == 33:
            x = community_chest(x)
        elif x == 7 or x == 22 or x == 36:
            x = c_hance(x)

        room[x] += 1

    sc = room[:]
    sc.sort()
    for i in range(0, 40):
        f = sc[i] / gg
        print(room.index(sc[i]), f)


if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    main(N)
