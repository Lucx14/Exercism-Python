num_mapping = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert(input_grid):
    validate_grid(input_grid)

    digits = []
    split_grid = [input_grid[x : x + 4] for x in range(0, len(input_grid), 4)]

    for batch in split_grid:
        grid = [[x[i : i + 3] for i in range(0, len(x), 3)] for x in batch]
        binaries = ["".join(x) for x in map(list, zip(*grid))]
        digits.append("".join(translate_binary(b) for b in binaries))

    return ",".join(digits)


def validate_grid(grid):
    if len(grid) % 4 != 0 or any(len(n) % 3 != 0 for n in grid):
        raise ValueError("Error: Check format of input grid")


def translate_binary(binary: str) -> str:
    if binary in num_mapping.keys():
        return num_mapping[binary]
    else:
        return "?"