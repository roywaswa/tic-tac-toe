
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0
        profile = f"{self.name} will be playing ({self.symbol}) \n Games Won: {self.score}"
        print(profile)

    def __str__(self):
        return f"Player {self.name} has score {self.score}"

    def __repr__(self):
        return f"Player({self.name}, {self.score})"

    def play(self):
        position = input(f"{self.name} enter a position to place {self.symbol}: ")
        return position.strip().capitalize()


