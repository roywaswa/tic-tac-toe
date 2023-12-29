from abstract_classes import Observable, Observer


class Game(Observable):

    def __init__(self):
        self.observers = []

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
        print(f"An Update has been sent: \n {args} \n {kwargs}")

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
        if right_evaluation:
            self.winner = previous_value
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
        if left_evaluation:
            self.winner = previous_value
        return left_evaluation

    def check_horizontal_win(self):
        horizontal_eval = bool()
        for row in range(len(self.rows)):
            pivot_comparator = None
            for col in range(len(self.columns)):
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
                self.winner = pivot_comparator
                break
        print(f"horizontal check : {horizontal_eval}")
        return horizontal_eval

    def check_vertical_win(self):
        vertical_eval = bool()
        for col in range(len(self.columns)):
            pivot_comparator = None
            for row in range(len(self.rows)):
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
