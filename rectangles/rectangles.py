def extract_corners(grid):
    result = []
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "+":
                result.append((i, j))
    return result


def vertically_aligned(coordiate_high, coordinate_low):
    return (
        coordinate_low[1] == coordiate_high[1] and coordinate_low[0] > coordiate_high[0]
    )


def horizontally_aligned(coordinate_left, coordinate_right):
    return (
        coordinate_left[0] == coordinate_right[0]
        and coordinate_right[1] > coordinate_left[1]
    )


def extract_square_coordinates(corners):
    rectangles = []
    for i, top_left in enumerate(corners):
        for top_right in corners[i + 1 :]:
            if horizontally_aligned(top_left, top_right):
                for j, bottom_left in enumerate(corners):
                    if vertically_aligned(top_left, bottom_left):
                        for bottom_right in corners[j + 1 :]:
                            if horizontally_aligned(
                                bottom_left, bottom_right
                            ) and vertically_aligned(top_right, bottom_right):
                                rect_coordinates = (
                                    top_left,
                                    top_right,
                                    bottom_left,
                                    bottom_right,
                                )
                                rectangles.append(rect_coordinates)
    return rectangles


def rectangles(strings):
    corners = extract_corners(strings)
    possible_squares = extract_square_coordinates(corners)
    return len(
        [
            coordinates
            for coordinates in possible_squares
            if validate(strings, coordinates)
        ]
    )


def validate(grid, coordinates):
    top = coordinates[0][0]
    bottom = coordinates[2][0]
    left = coordinates[0][1]
    right = coordinates[3][1]

    top_row = set(grid[top][left + 1 : right])
    bottom_row = set(grid[bottom][left + 1 : right])
    left_col = set([x[left] for x in grid][top + 1 : bottom])
    right_col = set([y[right] for y in grid][top + 1 : bottom])

    if " " in top_row or "|" in top_row:
        return False
    if " " in bottom_row or "|" in bottom_row:
        return False
    if " " in left_col or "-" in left_col:
        return False
    if " " in right_col or "-" in right_col:
        return False
    return True
