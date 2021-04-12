import string

alpha = string.ascii_lowercase


def encode(plain_text):
    return group_text(run_translation(clean_text(plain_text)), 5)


def decode(ciphered_text):
    return run_translation(clean_text(ciphered_text))


def run_translation(text):
    return "".join(atbash(l) if l in alpha else l for l in text)


def atbash(char):
    return alpha[25 - alpha.index(char)]


def clean_text(text):
    return "".join(l.lower() for l in text if l.isalnum())


def group_text(text, size):
    return " ".join((text[i : i + size]) for i in range(0, len(text), size))
