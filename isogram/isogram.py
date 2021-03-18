def is_isogram(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]

    return len(letters) == len(set(letters))
