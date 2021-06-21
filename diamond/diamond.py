import string

ALPHA = string.ascii_uppercase


def rows(letter):
    position = ALPHA.index(letter)
    max_width = (position * 2) + 1

    elements = ["A"]
    for i in range(1, position + 1):
        spaces = (i * 2) - 1
        elements.append(f"{ALPHA[i]}{spaces * ' '}{ALPHA[i]}")

    result = elements + list(reversed(elements))[1:]

    if max_width == 2:
        return result
    return [el.center(max_width) for el in result]
