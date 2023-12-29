from canvas import Canvas
from player import Player


def start_multiplayer_game():
    pl_x, pl_o = create_profiles()
    new_profile = False
    play_again = True
    while play_again:
        if new_profile:
            pl_x, pl_o = create_profiles()
        tic_tac_toe(pl_x, pl_o)
        play_again = True if list(input("Play again? \n[Y] Yes [N] No"))[0].capitalize() == "Y" else False
        if play_again is False:
            break
        else:
            new_profile = True if list(input("Create New Profiles? \n[Y] Yes [N] No"))[0].capitalize() == "Y" else False
    pass


def create_profiles() -> list[Player]:
    player_x = Player(input("Enter name for player X: "), "X")
    player_o = Player(input("Enter name for player O: "), "O")
    return [player_x, player_o]



def tic_tac_toe(x: Player, o: Player):
    # TIC-TAC-TOE
    print(f"""
    {x} vs \n{o}
    """)
    canvas = Canvas()
    rounds = int(1)
    while canvas.is_complete is False:
        print(f"Round: {rounds}")
        x_valid = True
        o_valid = True
        while x_valid:
            x_valid = not canvas.update_values(x, x.play())
            canvas.check_win()
        if canvas.is_complete:
            break
        while o_valid:
            o_valid = not canvas.update_values(o, o.play())
            canvas.check_win()
        if canvas.is_complete:
            break
        rounds += 1
    if canvas.winner == x.symbol:
        x.score += 1
        print(f"WINNER: {x}")
    if canvas.winner == o.symbol:
        o.score += 1
        print(f"WINNER: {x}")


