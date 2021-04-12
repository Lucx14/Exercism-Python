pairs = ("()", "[]", "{}")


def is_paired(input_string):
    brackets = "".join(x for x in input_string if x in "".join(pairs))

    if leftover_brackets(brackets):
        return False
    else:
        return True


def leftover_brackets(input_str: str):
    container = [input_str]
    while any(pair in container[0] for pair in pairs):
        for pair in pairs:
            updated = container[0].replace(pair, "")
            container[0] = updated

    return container[0]
