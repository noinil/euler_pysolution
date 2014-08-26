#!/usr/bin/env python

def poker_score(player):
    score = 0
    nums = []
    suits = []
    for i in player[:]:
        if i[0].isdigit():
            digi = int(i[0])
        elif i[0] == 'T':
            digi = 10
        elif i[0] == 'J':
            digi = 11
        elif i[0] == 'Q':
            digi = 12
        elif i[0] == 'K':
            digi = 13
        else:
            digi = 14
        suit = i[1]
        nums.append(digi)
        suits.append(suit)
    nums.sort()
    suits.sort()
    m = len(set(nums))
    n = len(set(suits))

    # set the scores!
    straight = 1 if m == 5 and nums[4] - nums[0] == 4 else 0
    flush = 1 if n == 1 else 0
    straight_flush = straight * flush
    if straight_flush == 1:
        return nums[4] * 100000000.0
    elif m == 2:
        for i in range(2, 15):
            if nums.count(i) == 4:
                return i * 10000000.0
            if nums.count(i) == 3:
                return i * 1000000.0
    elif flush == 1:
        return nums[4]*1000000 + nums[3]*60000 + nums[2]*4000 + nums[1]*200 + nums[0]
    elif straight == 1:
        return  100000.0 * nums[4]
    elif m == 3:
        local_list = []
        for i in range(2, 15):
            if nums.count(i) == 3:
                return i * 10000.0
            if nums.count(i) == 2:
                local_list.append(i)
        local_list.sort()
        return local_list[-1] * 1000 + local_list[0] * 60
    elif m == 4:
        for i in range(2, 15):
            if nums.count(i) == 2:
                score = i * 100
                nums.remove(i)
                nums.remove(i)
                break
        score = score + nums[2]/15 + nums[1]/15**2 + nums[0]/15**3
        return score
    else:
        score = nums[4]/15 + nums[3]/15**2 + nums[2]/15**3 + nums[1]/15**4 + nums[0]/15**5
        return score

def main():
    count = 0
    with open("../data/p54_poker.txt", "r") as f:
        for line in f:
            player_a = []
            player_b = []
            for piece in line.split()[:5]:
                player_a.append(piece)
            for piece in line.split()[5:]:
                player_b.append(piece)
            sa = poker_score(player_a)
            sb = poker_score(player_b)
            print("hand", player_a, "   ", player_b,  "sa = ", sa, "sb = ", sb)
            if sa > sb:
                count = count + 1
    print("Player 1 wins", count, "hands!")
if __name__ == '__main__':
    main()
