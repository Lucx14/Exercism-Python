def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for list in lists:
        for el in list:
            result += [el]

    return result


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    count = 0
    for _ in list:
        count += 1

    return count


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for i in range(len(list)):
        initial = function(initial, list[i])

    return initial


def foldr(function, list, initial):
    for i in range(len(list) - 1, -1, -1):
        initial = function(list[i], initial)

    return initial


def reverse(list):
    return [list[i] for i in range(len(list) - 1, -1, -1)]
