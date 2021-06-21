import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow,
    "cubed": None,
}
number_decorators = ("st", "nd", "rd", "th")
INPUT_ERROR = "Error: Input error"
UNSUPPORTED_OPERATION = "Error: Unsupported operation"


def answer(question):
    operations = parse_question(question)
    numbers = extract_ints(operations)
    operators = extract_ops(operations)
    validate_order_of_operations(operations, numbers, operators)

    result = numbers[0]

    for i in range(0, len(numbers) - 1):
        result = ops[operators[i]](result, numbers[i + 1])

    return result


def validate_order_of_operations(operations, numbers, operators):
    for i in range(0, len(operations) - 1):
        if i == "cubed":
            raise ValueError(UNSUPPORTED_OPERATION)
        if is_number(operations[i]):
            if not is_operator(operations[i + 1]):
                raise ValueError(INPUT_ERROR)
        elif is_operator(operations[i]):
            if not is_number(operations[i + 1]):
                raise ValueError(INPUT_ERROR)
    if len(numbers) != len(operators) + 1:
        raise ValueError(INPUT_ERROR)


def extract_ints(string_operations):
    return [int(n) for n in string_operations if n.replace("-", "").isdigit()]


def extract_ops(operations):
    return [o for o in operations if o in ops.keys()]


def is_number(string_num: str) -> bool:
    return string_num.replace("-", "").isdigit()


def is_operator(string_op: str) -> bool:
    return string_op in ops.keys()


def parse_question(question: str) -> list:
    operations = (
        (
            question.replace("What is", "")
            .replace("?", "")
            .replace("power", "")
            .replace("multiplied by", "*")
            .replace("divided by", "/")
            .replace("raised to the", "**")
            .replace("plus", "+")
            .replace("minus", "-")
        )
        .strip()
        .split()
    )

    for i, element in enumerate(operations):
        for y in number_decorators:
            if y in element:
                operations[i] = element[:-2]

    return operations
