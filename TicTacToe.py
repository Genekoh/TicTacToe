import random


class TicTacToe:
    def display_board(self, board):  # function to display the game board
        print(
            f"{board[7]}|{board[8]}|{board[9]}\n{board[4]}|{board[5]}|{board[6]}\n{board[1]}|{board[2]}|{board[3]}"
        )

    def player_input(self):  # function to determine the player's markers
        p1symbol = input("Player 1 choose a marker (X or O):\t")
        validinput = ["X", "x", "O", "o"]
        while p1symbol not in validinput:
            p1symbol = input("Please choose a valid input\t")
        p1symbol = p1symbol.upper()
        if p1symbol == "X":
            p2symbol = "O"
        elif p1symbol == "O":
            p2symbol = "X"
        return (p1symbol, p2symbol)

    def place_marker(self, board, marker, position):  # function to place marker
        board[position] = f"{marker}"

    def win_check(self, board, mark):  # function to check whether a marker has won

        return (
            (board[7] == mark and board[8] == mark and board[9] == mark)
            or (  # across the top
                board[4] == mark and board[5] == mark and board[6] == mark
            )
            or (  # across the middle
                board[1] == mark and board[2] == mark and board[3] == mark
            )
            or (  # across the bottom
                board[7] == mark and board[4] == mark and board[1] == mark
            )
            or (  # down the middle
                board[8] == mark and board[5] == mark and board[2] == mark
            )
            or (  # down the middle
                board[9] == mark and board[6] == mark and board[3] == mark
            )
            or (  # down the right side
                board[7] == mark and board[5] == mark and board[3] == mark
            )
            or (board[9] == mark and board[5] == mark and board[1] == mark)  # diagonal
        )  # diagonal

    def choose_first(self):  # function to choose who goes first
        number = random.randint(1, 2)
        return number

    def space_check(
        self, board, position
    ):  # function to check if the space/position is available
        if board[int(position)] != " ":
            return False
        else:
            return True

    def full_board_check(self, board):  # function to check if the board is full
        if " " not in board:
            return True
        else:
            return False

    def player_choice(self, board):  # function to ask a player's move
        position_range = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        move = input("Please choose your next position\t")
        while move not in position_range:
            move = input("Please choose a valid position\t")
        spacecheck = self.space_check(board, move)
        if spacecheck == True:
            pass
        else:
            while spacecheck != True:
                move = input("Please choose an empty position\t")
                spacecheck = self.space_check(board, move)
        return int(move)

    def replay(self):  # function to ask if players want to play again
        requestion = input("Do you want to play again? (Y or N)\t")
        while requestion not in ["Y", "y", "N", "n"]:
            requestion = input("Please choose a valid answer (Y or N)")
        if requestion in ["Y", "y"]:
            return True
        else:
            return False