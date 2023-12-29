import enum
from classes.game import Game, Evaluator
from classes.player import Profile, User, Player, Mark


class Commands(enum.Enum):
    QUIT = "q"
    HELP = "h"


def user_input(prompt: str):
    inpt = input(prompt)
    if list(inpt)[0] == "=":
        handle_command(command=inpt)
    return inpt


def display_help():
    print(f"""
    [=q] QUIT
    [=h] HELP
    """)
    return


def handle_command(command: str):
    command = command[1:].lower()[0]
    if command == Commands.QUIT.value:
        raise Exception("Game was Exited")
    elif command == Commands.HELP.value:
        display_help()
    else:
        raise ValueError("Invalid Command")


def create_new_profile() -> Profile:
    new_profile = Profile(
        name=user_input("Name: ")
    )
    new_user = User()
    new_user.register_user(new_profile, user_input("Password: "))
    return new_profile


def select_profile() -> Profile:
    user = User()
    user.get_user(user_input("Username: "), user_input("Password: "))
    return user.profile


def assign_player_marks(player_profiles: [Profile]):
    player_x = Player(Mark.X.value, player_profiles[0])
    player_o = Player(Mark.O.value, player_profiles[0])
    return player_x, player_o


def initiate_game(player_x: Player, player_o: Player):
    game = Game()
    evaluator = Evaluator()
    game.register_observer(evaluator)
    rounds = 1
    players = [player_x, player_o]
    while not evaluator.is_done:
        print(f"Round: {rounds}")
        for player in players:
            valid_play = True
            while valid_play:
                valid_play = player.play(user_input("Position:\n "))
            game.update_observers(game=game)
        rounds += 1


def generate_profile():
    """
    Prompt the user to select a saved profile or select from a number of profiles
    :return: a list of two profiles
    """
    player_profiles = [None, None]
    for index in range(2):
        while player_profiles[index] is None:
            profile_mode = user_input(f"Player {index + 1}\nSelect Profile Mode: \n[1]: Create New Profile \n[2]: "
                                      f"Select a profile")
            if profile_mode == "1":
                profile = create_new_profile()
                player_profiles[index] = profile
            elif profile_mode == "2":
                profile = select_profile()
                player_profiles[index] = profile
            else:
                print("Oops!!! \n It seems you have not made a valid choice. Input either (\"1\" or \"2\")")
    return player_profiles


def main():
    print(
        """
    Welcome to Tic Tac Toe!
    Mode: Multiplayer
    The game has been set to multiplayer, therefore, you require two players to play.
    """)
    player_profiles = generate_profile()
    is_done = bool()
    while not is_done:
        player_x, player_o = assign_player_marks(player_profiles)
        try:
            initiate_game(player_x, player_o)
        except Exception as e:
            print(e)
        valid_response = bool()
        while not valid_response:
            play_again = user_input("Would you like to play again? \n[Y]es [N]o ")
            if list(play_again.strip().capitalize())[0] == "Y":
                valid_response = bool()
                while not valid_response:
                    new_profiles = user_input("Select Profiles or maintain current profiles? \n[1] Keep Profiles [2] "
                                              "Select Profiles ")
                    if list(new_profiles.strip())[0] == "1":
                        is_done, valid_response = False, True
                    elif list(new_profiles.strip())[0] == "2":
                        player_profiles = generate_profile()
                        is_done, valid_response = False, True
                    else:
                        print("That is not a valid response!!!")
                        valid_response = False
                valid_response = True
            elif list(play_again.strip().capitalize())[0] == "N":
                is_done = True
                valid_response = True
            else:
                Exception("Invalid Response")
                valid_response = False


if __name__ == "__main__":
    main()
