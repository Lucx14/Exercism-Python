PREFIX = "This is"
SEPARATOR = " the "
THAT = "that"
DATA = [
    ("house", "Jack built."),
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
]


def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]


def verse(verse_number):
    v = [" ".join([DATA[i][0], THAT, DATA[i][1]]) for i in range(0, verse_number)]
    v.append(PREFIX)
    return SEPARATOR.join(v[::-1])
