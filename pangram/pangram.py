def is_pangram(sentence):
    return len(set(filter(str.isalpha, sentence.lower()))) == 26
