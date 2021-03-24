def score(word):
    VALUES = (
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"),
        ("D", "G"),
        ("B", "C", "M", "P"),
        ("F", "H", "V", "W", "Y"),
        ("K"),
        (),
        (),
        ("J", "X"),
        (),
        ("Q", "Z"),
    )
    score = 0
    for letter in word.upper():
        for i, values in enumerate(VALUES):
            if letter in values:
                score += i + 1
                break

    return score