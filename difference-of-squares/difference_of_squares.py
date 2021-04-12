def square_of_sum(number):
    return sum(range(0, number + 1)) ** 2


def sum_of_squares(number):
    return sum(num ** 2 for num in range(0, number + 1))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
