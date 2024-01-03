from models.abstract_classes import Observable, Observer

class Game(Observable):

    def __init__(self):
        self.observers = []
        self.grid_reference = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def check_validity(self, position: str):
        # todo: check if the move is in the list of valid reference
        if position not in self.grid_reference:
            return {"position": None, "is_valid": False}
        # todo: Convert the position to row and col
        position = list(position)
        row, column = position[0], position[1]
        row = ["A", "B", "C"].index(row)
        col = ["1", "2", "3"].index(column)
        # todo: Check if the specific reference has a value
        if self.grid[row][col] is not None:
            return {
                "position": None,
                "is_valid": False
            }
        # todo: Return position in terms of row and col
        return {
            "position": (row, col),
            "is_valid": True
        }

    def update_grid(self, position: tuple[int, int], mark: str):
        self.grid[position[0]][position[1]] = mark
        self.update_observers(grid=self.grid)

    def register_observer(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class Evaluator(Observer):

    def __init__(self):
        self.grid = [[], [], []]
        self.is_done = False

    def update(self, *args, **kwargs):
        grid = kwargs["grid"] if kwargs["grid"] else list()
        if len(grid) >= 1:
            self.grid = grid
        if (
                self.__check_right_diagonal_win() or
                self.__check_left_diagonal_win() or
                self.__check_vertical_win() or
                self.__check_horizontal_win()
        ):
            self.is_done = True
            raise Exception("Game is Done!!!")
        print(f"An Update has been sent: \n {grid}")

    def __check_right_diagonal_win(self):
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

    def __check_left_diagonal_win(self):
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

    def __check_horizontal_win(self):
        horizontal_eval = bool()
        for row in range(3):
            pivot_comparator = None
            for col in range(3):
                if self.grid[row][col] is None:
                    horizontal_eval = False
                    break
                elif pivot_comparator is None:
                    pivot_comparator = self.grid[row][col]
                    continue
                if pivot_comparator == self.grid[row][col]:
                    horizontal_eval = True
                    pivot_comparator = self.grid[row][col]
                else:
                    horizontal_eval = False
                    break
            if horizontal_eval is True:
                break
        return horizontal_eval

    def __check_vertical_win(self):
        vertical_eval = bool()
        for col in range(3):
            pivot_comparator = None
            for row in range(3):
                if self.grid[row][col] is None:
                    vertical_eval = False
                    break
                elif pivot_comparator is None:
                    pivot_comparator = self.grid[row][col]
                    continue
                if pivot_comparator == self.grid[row][col]:
                    vertical_eval = True
                    pivot_comparator = self.grid[row][col]
                else:
                    vertical_eval = False
                    break
            if vertical_eval is True:
                break
        print(f"vertical check : {vertical_eval}")
        return vertical_eval
