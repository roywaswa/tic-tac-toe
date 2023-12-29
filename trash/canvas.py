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
        self.winner = str()

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
                    break
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

