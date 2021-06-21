ELEMENTS = [
    ("#", "a Partridge in a Pear Tree."),
    ("first", "and a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves, "),
    ("third", "three French Hens, "),
    ("fourth", "four Calling Birds, "),
    ("fifth", "five Gold Rings, "),
    ("sixth", "six Geese-a-Laying, "),
    ("seventh", "seven Swans-a-Swimming, "),
    ("eighth", "eight Maids-a-Milking, "),
    ("ninth", "nine Ladies Dancing, "),
    ("tenth", "ten Lords-a-Leaping, "),
    ("eleventh", "eleven Pipers Piping, "),
    ("twelfth", "twelve Drummers Drumming, "),
]
PREFIX = ("On the ", " day of Christmas my true love gave to me: ")


def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]


def verse(day):
    result = [prefix(day)]
    if day == 1:
        result.append(ELEMENTS[0][1])
    else:
        result.extend([ELEMENTS[i][1] for i in range(day, 0, -1)])
    return "".join(result)


def prefix(day):
    return f"{PREFIX[0]}{ELEMENTS[day][0]}{PREFIX[1]}"