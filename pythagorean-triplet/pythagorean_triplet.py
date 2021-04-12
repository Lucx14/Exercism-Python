import math

# This vid was helpful for the math
# https://www.youtube.com/watch?v=OisUvx0RKFI


def triplets_with_sum(number):
    triplets = []
    for c in range(1, number // 2):
        sum_a_b = number - c
        if (2 * sum_a_b) ** 2 - 8 * (sum_a_b ** 2 - c ** 2) > 0:
            a, b = calculate_unknown_sides(c, sum_a_b)
            if is_pythagorean_triplet(a, b, c):
                triplets.append([a, b, c])

    return triplets


def calculate_unknown_sides(c, sum_a_b):
    s = 2 * sum_a_b
    q = (s ** 2) - 8 * (sum_a_b ** 2 - c ** 2)

    a = int((s - math.sqrt(q)) / 4)
    b = int((s + math.sqrt(q)) / 4)

    return (a, b)


def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2
