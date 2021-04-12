from functools import reduce
from math import sqrt

input_error = "Input must be a positive integer"
perfect = "perfect"
abundant = "abundant"
deficient = "deficient"


def classify(number):
    if number < 1:
        raise ValueError(input_error)

    sum_of_factors = aliquot_sum(number)

    return run_classification(number, sum_of_factors)


def aliquot_sum(number):
    result = set(
        reduce(
            list.__add__,
            (
                [i, number // i]
                for i in range(1, int(sqrt(number)) + 1)
                if number % i == 0
            ),
        )
    )
    result.remove(number)
    return sum(result)


def run_classification(number, sum_of_factors):
    if sum_of_factors == number:
        return perfect
    if sum_of_factors > number:
        return abundant
    if sum_of_factors < number:
        return deficient
