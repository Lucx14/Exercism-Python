import numpy as np

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot:
    right_turn = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}
    left_turn = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}

    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, commands):
        for command in commands:
            self.process_move(command)

    def process_move(self, move):
        if move == "A":
            self.advance()
        elif move == "R":
            self.turn_right()
        elif move == "L":
            self.turn_left()

    def turn_right(self):
        self.direction = self.right_turn[self.direction]

    def turn_left(self):
        self.direction = self.left_turn[self.direction]

    def advance(self):
        self.coordinates = tuple(np.add(self.coordinates, self.direction))
