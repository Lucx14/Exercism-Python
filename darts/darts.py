def score(x, y):
    r = (x ** 2 + y ** 2) ** 0.5

    if r > 10:
        return 0
    elif r > 5:
        return 1
    elif r > 1:
        return 5
    else:
        return 10