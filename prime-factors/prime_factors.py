import math


def factors(value):
    result = []

    while value % 2 == 0:
        result.append(2)
        value /= 2

    for n in range(3, int(math.sqrt(value)) + 1, 2):
        while value % n == 0:
            result.append(n)
            value /= n

    if value > 2:
        result.append(value)

    return result
