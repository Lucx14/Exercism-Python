import string

alphabet = string.ascii_lowercase


def rotate(text, key):
    return "".join(shift(char, key) if char.isalpha() else char for char in text)


def shift(letter, key):
    char = letter.lower()
    tr = char.maketrans(alphabet, alphabet[key:] + alphabet[:key])
    encoded = char.translate(tr)
    return encoded.upper() if letter.isupper() else encoded
