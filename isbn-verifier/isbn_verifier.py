import re
from functools import reduce

ISBN_PATTERN = re.compile(r"^\d{9}(\d|X)$")


def is_valid(isbn):
    cleaned_isbn = isbn.replace("-", "")

    if not re.search(ISBN_PATTERN, cleaned_isbn):
        return False

    check = cleaned_isbn[-1]
    numbers = [(int(n) * (10 - i)) for i, n in enumerate(cleaned_isbn[:-1])]
    check_value = 10 if check == "X" else int(check)
    numbers.append(check_value)

    return reduce(lambda a, b: a + b, numbers) % 11 == 0
