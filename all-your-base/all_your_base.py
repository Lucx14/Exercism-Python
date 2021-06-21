from typing import List

BINARY = 2
BASE_ERROR = "Error: Input/Output base cannot be less than 2"
DIGIT_ERROR = "Error: Invalid digits"


def rebase(input_base: int, digits: List[int], output_base: int) -> List[int]:
    if input_base < BINARY or output_base < BINARY:
        raise ValueError(BASE_ERROR)
    if any(digit < 0 for digit in digits):
        raise ValueError(DIGIT_ERROR)
    if any(digit >= input_base for digit in digits):
        raise ValueError(DIGIT_ERROR)

    return from_decimal(to_decimal(digits, input_base), output_base)


def to_decimal(num: List[int], input_base: int) -> List[int]:
    result = sum(
        [digit * input_base ** ((len(num) - 1) - idx) for idx, digit in enumerate(num)]
    )
    return [int(x) for x in list(str(result))]


def from_decimal(digits: List[int], target_base: int) -> List[int]:
    buffer = []
    decimal = int("".join([str(x) for x in digits]))

    if decimal == 0:
        return [decimal]

    while decimal > 0:
        quotient, remainder = divmod(decimal, target_base)
        decimal = quotient
        buffer.append(remainder)

    return list(reversed(buffer))
