import itertools


def transpose(lines):
    matrix = [list(t.replace(" ", "*")) for t in lines.splitlines()]

    return "\n".join(
        "".join(group).rstrip().replace("*", " ")
        for group in itertools.zip_longest(*matrix, fillvalue=" ")
    )
