def sum_of_multiples(limit, multiples):
    return sum(
        {
            n
            for multiple in multiples
            if multiple != 0
            for n in range(multiple, limit, multiple)
        }
    )
