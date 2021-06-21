import math


def find(search_list, value):
    l = 0
    r = len(search_list) - 1

    while r >= l:
        idx = l + math.floor((r - l) / 2)
        val = search_list[idx]
        if val == value:
            return idx
        elif val > value:
            r = idx - 1
        else:
            l = idx + 1

    raise ValueError("Value not in list")
