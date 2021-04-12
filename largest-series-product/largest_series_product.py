from functools import reduce
from typing import List

ERROR_MESSAGE = [
    "Input Error: Size must be a positive value",
    "Input Error: Cannot submit empty series with a positive size",
    "Input Error: Size cannot be greater than the length of the series",
    "Input Error: Series must be a numeric string"
]


def largest_product(series, size):
    validate_inputs(series, size)

    if size == 0:
        return 1

    return max(
        [multiply(generate_numbers(group)) for group in split_by_size(series, size)]
    )


def multiply(elements: List[int]) -> int:
    return reduce((lambda x, y: x * y), elements)


def generate_numbers(numeric_text: str) -> List[int]:
    return [int(n) for n in list(numeric_text)]


def split_by_size(numeric_text: str, size: int) -> List[str]:
    return [numeric_text[i: i + size] for i in range(0, len(numeric_text) + 1 - size)]


def validate_inputs(series, size):
    if size < 0:
        raise ValueError(ERROR_MESSAGE[0])
    if size > 0 and series == "":
        raise ValueError(ERROR_MESSAGE[1])
    if size > len(series):
        raise ValueError(ERROR_MESSAGE[2])
    if series and not series.isnumeric():
        raise ValueError(ERROR_MESSAGE[3])
