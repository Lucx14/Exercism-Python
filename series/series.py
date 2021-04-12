def slices(series, length):
    if length not in range(1, len(series) + 1):
        raise ValueError("Error: Length not valid")
    substrings = []
    while len(series) >= length:
        substrings.append(series[:length])
        series = series[1:]

    return substrings
