def primes(limit):
    sample = [[num, False] for num in range(2, limit + 1)]

    for num in sample:
        if num[1] == True:
            continue

        for n in sample:
            if n[0] in range(num[0], limit + 1, num[0])[1:]:
                n[1] = True

    return [p[0] for p in sample if p[1] == False]
