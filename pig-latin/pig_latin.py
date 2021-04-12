VOWELS = ("a", "e", "i", "o", "u")
SPECIALS = ("xr", "yt")


def translate(text):
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    if word.startswith(SPECIALS):
        return format_pig_latin(word[:2], word[2:])
    elif word.startswith("y"):
        return format_pig_latin(word[1:], word[:1])
    elif word.startswith(VOWELS):
        return format_pig_latin(word[:1], word[1:])
    else:
        i = first_vowel_index(word)
        return format_pig_latin(word[i:], word[:i])


def format_pig_latin(start, middle, end="ay"):
    return "".join([start, middle, end])


def typeof_vowel(letter):
    return letter in VOWELS or letter == "y"


def qu_detected(letter, index, word):
    return letter == "u" and index > 0 and word[index - 1] == "q"


def first_vowel_index(word):
    for i, letter in enumerate(word):
        if qu_detected(letter, i, word):
            continue
        if typeof_vowel(letter):
            return i
