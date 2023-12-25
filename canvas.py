from player import Player


class Canvas:
    def __init__(self):
        self.is_complete = False
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.rows = ["A", "B", "C"]
        self.columns = ["1", "2", "3"]
        self.grid_reference = {
            "A1": self.grid[0][0],
            "A2": self.grid[0][1],
            "A3": self.grid[0][2],
            "B1": self.grid[1][0],
            "B2": self.grid[1][1],
            "B3": self.grid[1][2],
            "C1": self.grid[2][0],
            "C2": self.grid[2][1],
            "C3": self.grid[2][2]
        }

    def __str__(self):
        cnv = f"""
        {self.grid[0][0]}|{self.grid[0][1]}|{self.grid[0][2]}
        -----
        {self.grid[1][0]}|{self.grid[1][1]}|{self.grid[1][2]}
        -----
        {self.grid[2][0]}|{self.grid[2][1]}|{self.grid[2][2]}
        """
        return cnv

    def show_reference(self):
        print("Reference Grid")
        canvas_copy = self.grid.copy()
        for row in range(len(self.rows)):
            for column in range(len(self.columns)):
                canvas_copy[row][column] = f"{self.rows[row]}{self.columns[column]}"
        cnv = f"""
        {canvas_copy[0][0]}|{canvas_copy[0][1]}|{canvas_copy[0][2]}
        - + - + -
        {canvas_copy[1][0]}|{canvas_copy[1][1]}|{canvas_copy[1][2]}
        - + - + -
        {canvas_copy[2][0]}|{canvas_copy[2][1]}|{canvas_copy[2][2]}
        """
        print(cnv)

    def __extract_position__(self, position: str):
        position = list(position)
        row, column = position[0], position[1]
        row = self.rows.index(row)
        column = self.columns.index(column)
        return row, column

    def update_values(self, player: Player, position: str):
        move_is_valid = self.check_move_validity(position)
        if move_is_valid:
            row, column = self.__extract_position__(position)
            self.grid[row][column] = player.symbol
            print(f"{player.name} has placed {player.symbol} at {position}")
            print(self)
            if self.has_valid_moves() is False:
                self.is_complete = True
            return True
        else:
            return False

    def has_valid_moves(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is None:
                    count += 1
        return True if count > 0 else False

    def check_move_validity(self, position) -> bool:
        if position in self.grid_reference.keys():
            row, col = self.__extract_position__(position)
            if self.grid[row][col] is None:
                return True
            else:
                return False
        else:
            return False

    def check_right_diagonal_win(self):
        right_evaluation = bool()
        previous_value = ""
        for i in range(3):
            if previous_value == "":
                previous_value = self.grid[i][i]
                if previous_value is None:
                    right_evaluation = False
                    break
            elif previous_value is self.grid[i][i]:
                right_evaluation = True
            else:
                right_evaluation = False
                break
        return right_evaluation

    def check_left_diagonal_win(self):
        left_evaluation = bool()
        previous_value = ""
        n = 2
        for i in range(n + 1):
            if previous_value == "":
                previous_value = self.grid[i][abs(i - n)]
                if previous_value is None:
                    left_evaluation = False
                    break
            elif previous_value is self.grid[i][abs(i - n)]:
                left_evaluation = True
                previous_value = self.grid[i][abs(i - n)]
            else:
                left_evaluation = False
                break
        return left_evaluation

    def check_horizontal_win(self):
        horizontal_eval = bool()
        cols = 0
        for i in range(len(self.rows)):
            if self.grid[i][cols] == self.grid[i][cols - 1] == self.grid[i][cols - 2]\
                    and (self.grid[i][cols] is not None):
                horizontal_eval = True
                print("Horizontal is True")
        cols += 1
        return horizontal_eval

    def check_vertical_win(self):
        vertical_eval = bool()
        row = 0
        for i in range(len(self.columns)):
            if self.grid[row][i] == self.grid[row-1][i] == self.grid[row-2][i]\
                    and (self.grid[row][i] is not None):
                vertical_eval = True
                print("Vertical Is True")
            row += 1
        return vertical_eval

    def check_win(self):
        win = (
                self.check_left_diagonal_win() or
                self.check_right_diagonal_win() or
                self.check_vertical_win() or
                self.check_horizontal_win()
        )
        self.is_complete = win
        return win
