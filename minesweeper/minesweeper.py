def annotate(minefield):
    validate_minefield(minefield)

    board = [
        [el if el == "*" else 0 for el in row]
        for row in [list(row) for row in minefield]
    ]

    # rows
    for row in board:
        for i, val in enumerate(row):
            if val == "*" or len(row) == 1:
                continue
            elif i == 0:
                if row[i + 1] == "*":
                    row[i] += 1
            elif i == len(row) - 1:
                if row[i - 1] == "*":
                    row[i] += 1
            else:
                if row[i - 1] == "*":
                    row[i] += 1
                if row[i + 1] == "*":
                    row[i] += 1

    if len(minefield) <= 1:
        result = [
            [" " if y == "0" else y for y in row]
            for row in [[str(x) for x in row] for row in board]
        ]

        return ["".join(r) for r in result]

    # if multiple rows....
    else:
        trans = [list(t) for t in list(zip(*board))]

        for col in trans:
            for i, val in enumerate(col):
                if val == "*":
                    continue
                elif i == 0:
                    if col[i + 1] == "*":
                        col[i] += 1
                elif i == len(col) - 1:
                    if col[i - 1] == "*":
                        col[i] += 1
                else:
                    if col[i - 1] == "*":
                        col[i] += 1
                    if col[i + 1] == "*":
                        col[i] += 1

        revert = [list(t) for t in list(zip(*trans))]

        # Diagonals
        for i, row in enumerate(revert):
            for p, val in enumerate(row):
                if val == "*" or len(row) == 1:
                    continue
                if i == 0:
                    if p == 0:
                        if revert[i + 1][p + 1] == "*":
                            row[p] += 1
                    elif p == len(row) - 1:
                        if revert[i + 1][p - 1] == "*":
                            row[p] += 1
                    else:
                        if revert[i + 1][p + 1] == "*":
                            row[p] += 1
                        if revert[i + 1][p - 1] == "*":
                            row[p] += 1
                elif i == len(revert) - 1:
                    if p == 0:
                        if revert[i - 1][p + 1] == "*":
                            row[p] += 1
                    elif p == len(row) - 1:
                        if revert[i - 1][p - 1] == "*":
                            row[p] += 1
                    else:
                        if revert[i - 1][p + 1] == "*":
                            row[p] += 1
                        if revert[i - 1][p - 1] == "*":
                            row[p] += 1
                else:
                    if p == 0:
                        if revert[i + 1][p + 1] == "*":
                            row[p] += 1
                        if revert[i - 1][p + 1] == "*":
                            row[p] += 1
                    elif p == len(row) - 1:
                        if revert[i + 1][p - 1] == "*":
                            row[p] += 1
                        if revert[i - 1][p - 1] == "*":
                            row[p] += 1
                    else:
                        if revert[i - 1][p + 1] == "*":
                            row[p] += 1
                        if revert[i - 1][p - 1] == "*":
                            row[p] += 1
                        if revert[i + 1][p + 1] == "*":
                            row[p] += 1
                        if revert[i + 1][p - 1] == "*":
                            row[p] += 1

    result = [
        [" " if y == "0" else y for y in row]
        for row in [[str(x) for x in row] for row in revert]
    ]

    return ["".join(r) for r in result]


def validate_minefield(minefield):
    # validation 1
    if len(set([len(x) for x in minefield])) > 1:
        raise ValueError("Error: uneven board")

    # validation 2
    valid_chars = [" ", "*"]
    all_given_chars = list("".join(minefield))
    for char in all_given_chars:
        if char not in valid_chars:
            raise ValueError("Error: invalid characters in board")
