from gameflow import start_multiplayer_game


def prompt_game():
    print("""
    Welcome to Tic Tac Toe!
    Mode: Multiplayer
    The game has been set to multiplayer, therefore, you require two players to play.
    """)
    start_multiplayer_game()


if __name__ == "__main__":
    prompt_game()
