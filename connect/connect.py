import operator


UP_LEFT = (-1, 0)
UP_RIGHT = (-1, 2)
RIGHT = (0, 2)
LEFT = (0, -2)
DOWN_LEFT = (1, -2)
DOWN_RIGHT = (1, 0)
HORIZONTAL = "horizontal"
VERTICAL = "vertical"


class ConnectGame:
    def __init__(self, board):
        self.board = [row.strip() for row in board.split("\n")]

    def get_winner(self):
        return self._x_wins() or self._o_wins() or ""

    def _x_wins(self):
        for i in range(len(self.board)):
            if self.board[i][0] == "X" and self._X_runner((i, 0)):
                return "X"

    def _o_wins(self):
        for i in range(len(self.board[0])):
            if self.board[0][i] == "O" and self._O_runner((0, i)):
                return "O"

    def _look(self, direction, position):
        r, c = self._move(direction, position)
        return self.board[r][c]

    def _move(self, direction, position):
        return tuple(map(operator.add, position, direction))

    def _finished(self, position, direction):
        r, c = position
        if direction == HORIZONTAL:
            return c == len(self.board[0]) - 1
        else:
            return r == len(self.board) - 1

    def _X_runner(self, position):
        history = []
        history.append(position)
        while not self._finished(position, HORIZONTAL):
            row, _ = position
            if (
                self._look(RIGHT, position) == "X"
                and self._move(RIGHT, position) not in history
            ):
                position = self._move(RIGHT, position)
            elif (
                self._look(LEFT, position) == "X"
                and self._move(LEFT, position) not in history
            ):
                position = self._move(LEFT, position)
            elif (
                row > 0
                and self._look(UP_LEFT, position) == "X"
                and self._move(UP_LEFT, position) not in history
            ):
                position = self._move(UP_LEFT, position)
            elif (
                row > 0
                and self._look(UP_RIGHT, position) == "X"
                and self._move(UP_RIGHT, position) not in history
            ):
                position = self._move(UP_RIGHT, position)
            elif (
                row < len(self.board) - 1
                and self._look(DOWN_RIGHT, position) == "X"
                and self._move(DOWN_RIGHT, position) not in history
            ):
                position = self._move(DOWN_RIGHT, position)
            elif (
                row < len(self.board) - 1
                and self._look(DOWN_LEFT, position) == "X"
                and self._move(DOWN_LEFT, position) not in history
            ):
                position = self._move(DOWN_LEFT, position)
            else:
                break
            history.append(position)

        if self._finished(position, HORIZONTAL):
            return True

    def _O_runner(self, position):
        history = []
        history.append(position)
        while not self._finished(position, VERTICAL):
            row, col = position
            if (
                self._look(DOWN_RIGHT, position) == "O"
                and self._move(DOWN_RIGHT, position) not in history
            ):
                position = self._move(DOWN_RIGHT, position)
            elif (
                col > 1
                and self._look(DOWN_LEFT, position) == "O"
                and self._move(DOWN_LEFT, position) not in history
            ):
                position = self._move(DOWN_LEFT, position)
            elif (
                col < len(self.board[0]) - 2
                and self._look(RIGHT, position) == "O"
                and self._move(RIGHT, position) not in history
            ):
                position = self._move(RIGHT, position)
            elif (
                col > 1
                and self._look(LEFT, position) == "O"
                and self._move(LEFT, position) not in history
            ):
                position = self._move(LEFT, position)
            elif (
                row > 0
                and self._look(UP_LEFT, position) == "O"
                and self._move(UP_LEFT, position) not in history
            ):
                position = self._move(UP_LEFT, position)
            elif (
                row > 0
                and col > len(self.board[0]) - 2
                and self._look(UP_RIGHT, position) == "O"
                and self._move(UP_RIGHT, position) not in history
            ):
                position = self._move(UP_RIGHT, position)
            else:
                break
            history.append(position)

        if self._finished(position, VERTICAL):
            return True
