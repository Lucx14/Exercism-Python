def find_anagrams(word, candidates):
    return [c for c in candidates if is_anagram((word, c))]


def is_anagram(test_subjects):
    word, candidate = (s.lower() for s in test_subjects)
    return sorted(word) == sorted(candidate) and word != candidate
