from TicTacToe import TicTacToe

# ----- START OF GAME -----
print("Welcome to Tic Tac Toe!")
Game = TicTacToe()
while True:
    Game.position_range = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]  # Set the game up here
    game_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    test_board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Game.display_board(test_board)
    game_on = True
    p1symbol, p2symbol = Game.player_input()
    first_player = Game.choose_first()
    if first_player == 1:
        second_player = 2
        first_marker = p1symbol
        second_marker = p2symbol
    else:
        second_player = 1
        first_marker = p2symbol
        second_marker = p1symbol
    print(
        f"Player {first_player} is {first_marker} and Player {second_player} is {second_marker}, player {first_player} going first\n"
    )
    Game.display_board(game_board)
    # pass

    while game_on == True:
        # Player 1 Turn
        fullboardcheck = Game.full_board_check(game_board)
        if fullboardcheck == True:
            print("Board is full, it is a draw\n")
            break
        else:
            first_move = Game.player_choice(game_board)
            Game.place_marker(game_board, first_marker, first_move)
            Game.display_board(game_board)
            wincheck = Game.win_check(game_board, first_marker)
        if wincheck == True:
            print(f"Player {first_player} has won\nGame over.\n")
            break
        else:
            pass
        # Player2's turn.
        fullboardcheck = Game.full_board_check(game_board)
        if fullboardcheck == True:
            print("Board is full, it is a draw\n")
            break
        else:
            second_move = Game.player_choice(game_board)
            Game.place_marker(game_board, second_marker, second_move)
            Game.display_board(game_board)
            wincheck = Game.win_check(game_board, second_marker)
        if wincheck == True:
            print(f"Player {second_player} has won\nGame over.\n")
            break
        else:
            pass
        # pass
    replayquestion = Game.replay()
    if replayquestion:
        print("\n" * 100)
        continue
    else:
        print("turning off")
        break
