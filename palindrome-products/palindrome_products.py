from itertools import combinations_with_replacement


def largest(min_factor, max_factor):
    palindromes = detect_palindromes(min_factor, max_factor)
    if not palindromes:
        return (None, [])
    largest_palindrome = max(palindromes)

    return [largest_palindrome, palindromes[largest_palindrome]]


def smallest(min_factor, max_factor):
    palindromes = detect_palindromes(min_factor, max_factor)
    if not palindromes:
        return (None, [])

    smallest_palindrome = min(palindromes)

    return [smallest_palindrome, palindromes[smallest_palindrome]]


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def validate_input(factors):
    if factors[0] > factors[1]:
        raise ValueError("Argument Error: Min factor must be smaller than max factor")


def detect_palindromes(min_factor, max_factor):
    validate_input((min_factor, max_factor))

    result = {}
    for i in combinations_with_replacement(list(range(min_factor, max_factor + 1)), 2):
        product = i[0] * i[1]
        if is_palindrome(product):
            if product in result:
                result[product].append([i[0], i[1]])
            else:
                result[product] = [[i[0], i[1]]]

    return result
