class Queen:
    def __init__(self, row, column):
        if not (0 <= row < 8 and 0 <= column < 8):
            raise ValueError("Error: position not on the board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Error: cannot occupy the same position on board")
        if (
            self.row == another_queen.row
            or self.column == another_queen.column
            or abs(self.row - another_queen.row)
            == abs(self.column - another_queen.column)
        ):
            return True

        return False
