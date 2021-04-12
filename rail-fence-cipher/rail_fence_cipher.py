def encode(message, rails):
    res = apply_rails(message, rails)

    return "".join("".join(section) for section in res)


def decode(encoded_message, rails):
    slices = slices_for_decode(encoded_message, rails)
    result = []

    pointer = 0
    direction = 1
    while len(result) < len(encoded_message):
        result.append(slices[pointer][0])
        slices[pointer].pop(0)

        if pointer == len(slices) - 1:
            direction = -1
        elif pointer == 0:
            direction = 1

        pointer += direction

    return "".join(result)


def apply_rails(text, rails):
    results = []
    for i in range(rails):
        results.append([])

    pointer = 0
    direction = 1
    for letter in text:
        results[pointer].append(letter)
        if pointer == rails - 1:
            direction = -1
        elif pointer == 0:
            direction = 1

        pointer += direction

    return results


def slices_for_decode(encoded_message, rails):
    sizes = [len(x) for x in apply_rails(encoded_message, rails)]

    return [list(encoded_message[s[0] : s[1]]) for s in sizes_to_slices(sizes)]


def sizes_to_slices(sizes):
    slice_coordinates = []
    acc = 0
    for s in sizes:
        slice_coordinates.append((acc, s + acc))
        acc += s

    return slice_coordinates
