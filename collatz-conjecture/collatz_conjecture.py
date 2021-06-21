def steps(number):
    if number <= 0:
        raise ValueError("Input must be a positive int")

    steps = 0
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (number * 3) + 1
        steps += 1
    return steps
