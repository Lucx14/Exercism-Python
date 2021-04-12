import math
import itertools


def cipher_text(plain_text):
    clean_text = normalized(plain_text)
    if len(clean_text) == 0:
        return ""

    c = math.ceil(math.sqrt(len(clean_text)))

    return transpose_text(clean_text, c)


def normalized(text):
    return "".join(map(lambda letter: letter if letter.isalnum() else "", text)).lower()


def transpose_text(text, column_size):
    return " ".join(
        "".join(text)
        for text in list(
            map(
                list,
                itertools.zip_longest(*chunk_text(text, column_size), fillvalue=" "),
            )
        )
    )


def chunk_text(text, chunk_size):
    return [list(text[i : i + chunk_size]) for i in range(0, len(text), chunk_size)]
