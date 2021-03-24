import re


def abbreviate(words):
    pattern = re.compile(r"\b\w")
    cleaned = re.sub("[_|']", "", words).upper()

    return "".join(pattern.findall(cleaned))
