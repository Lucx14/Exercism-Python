def saddle_points(matrix):
    if irregular_matrix(matrix):
        raise ValueError("Error")

    rows = matrix
    cols = transpose_matrix(matrix)
    result = []

    for i, row in enumerate(rows):
        max_in_row = max(row)
        positions_of_max = [i for i, v in enumerate(row) if v == max_in_row]
        for c in positions_of_max:
            column = cols[c]
            min_in_col = min(column)
            if min_in_col == max_in_row:
                result.append({"row": i + 1, "column": c + 1})

    return result


def transpose_matrix(matrix):
    zipped_rows = zip(*matrix)
    return [list(row) for row in zipped_rows]


def irregular_matrix(matrix):
    return len(set([len(r) for r in matrix])) > 1
