from collections import Counter


def top_count(dice):
    return Counter(dice).most_common(1)[0]


def three_of_a_kind(dice):
    return top_count(dice)[1] == 3


def four_of_a_kind(dice):
    return top_count(dice)[1] >= 4


def five_of_a_kind(dice):
    return top_count(dice)[1] == 5


def which_four(dice):
    return top_count(dice)[0]


def calc(d, r):
    return d.count(r) * r


CHOICE = lambda dice: sum(dice)
ONES = lambda dice: calc(dice, 1)
TWOS = lambda dice: calc(dice, 2)
THREES = lambda dice: calc(dice, 3)
FOURS = lambda dice: calc(dice, 4)
FIVES = lambda dice: calc(dice, 5)
SIXES = lambda dice: calc(dice, 6)
FULL_HOUSE = lambda dice: sum(dice) if three_of_a_kind(dice) else 0
FOUR_OF_A_KIND = lambda dice: 4 * which_four(dice) if four_of_a_kind(dice) else 0
YACHT = lambda dice: 50 if five_of_a_kind(dice) else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def score(dice, category):
    return category(dice)
