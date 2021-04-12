numerals = (
    ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
    ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
    ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
    ("", "M", "MM", "MMM"),
)


def roman(number):
    return "".join(
        [
            numerals[i][int(val)]
            for i, val in enumerate(str(number).rjust(4, "0")[::-1])
        ][::-1]
    )
