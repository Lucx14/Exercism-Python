import re
from collections import Counter


def count_words(sentence):
    return Counter(re.findall(r"[\w]+(?:'\w)*", sentence.lower().replace("_", " ")))
