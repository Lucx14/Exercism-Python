def square(number):
    if number not in range(1, 65):
        raise ValueError("Error: number out of range")
    return 2**(number - 1)


def total():
    return sum(square(n) for n in range(1, 65))
