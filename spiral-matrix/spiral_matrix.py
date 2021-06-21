import operator
from collections import deque


def spiral_matrix(size):
    grid = [[None for j in range(0, size)] for i in range(0, size)]
    position = (0, 0)
    counter = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirs = deque(directions)
    return recurse_the_matrix(grid, position, counter, dirs)


def recurse_the_matrix(grid, position, counter, directions):
    current_direction = directions[0]
    row, col = position

    # Exit condition: Grid is full of numbers and no Nones
    if not any(None in sublist for sublist in grid):
        return grid

    # Recursion conditions:

    # 1: you have gone too far so you need to backtrack, change direction and then recurse
    if out_of_bounds(position, grid) or grid[row][col] is not None:
        position = go_back(position, current_direction)
        directions.rotate(-1)
        position = advance(position, directions[0])
        return recurse_the_matrix(grid, position, counter, directions)

    # 2: position looks good, mark it, advance the position and recurse
    grid[row][col] = counter
    counter += 1
    position = advance(position, current_direction)
    return recurse_the_matrix(grid, position, counter, directions)


def out_of_bounds(position, grid):
    r, c = position
    return r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1


def advance(position, direction):
    return tuple(map(operator.add, position, direction))


def go_back(position, direction):
    return tuple(map(operator.sub, position, direction))