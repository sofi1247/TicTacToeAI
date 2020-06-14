from abc import ABC, abstractmethod
from copy import deepcopy


class Player(ABC):
    @abstractmethod
    def make_move(self, board):
        pass


class Human(Player):

    def __init__(self, piece):
        self.name = input("Enter your name please: ")
        self.my_piece = piece

    def make_move(self, board):

        try:
            row_num = int(input("Enter a row number between 0 and 2: "))
            col_num = int(input("Enter a column number between 0 and 2: "))
        except ValueError:
            print("Invalid symbol. Please enter a number.")
            return self.make_move(board)

        if board[row_num][col_num] == "n":
            return row_num, col_num
        else:
            print("This tile is already filled. Please choose another one.")
            return self.make_move(board)


class AI(Player):

    def __init__(self, piece):
        self.name = "AI-S"
        self.my_piece = piece

    def make_move(self, board):
        board2 = deepcopy(board)
        if self.my_piece == "x":
            opponent_piece = "o"
        else:
            opponent_piece = "x"

        turn = checking(self, board)

        if turn == 0:
            return 1, 1
        elif turn == 1:
            if board2[1][1] == "n":
                return 1, 1
            else:
                return 0, 2
        elif turn == 2:
            if board2[0][0] == opponent_piece or board2[0][0] == opponent_piece:
                return 0, 2
            elif board2[0][2] == opponent_piece or board2[2][0] == opponent_piece:
                return 2, 2
            else:
                return 2, 2
        else:
            if potential_win(self, board) != "no win":
                return potential_win(self, board)
            else:
                result = checking_threat(self, board)
                for i in range(0, len(result)):
                    if result[i] != [9,9]:
                        my_move = checking_threat(self, board)[i]
                        break
                    else:
                        my_move = random_move(self, board)
                return my_move

def checking(self, board):
    board1 = deepcopy(board)
    free_tiles = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if board1[i][j] == "n":
                free_tiles += 1

    turn = 9 - free_tiles

    return turn

def checking_threat(self, board):
    board1 = deepcopy(board)
    move = []

    if self.my_piece == "x":
        opponent_piece = "o"
    elif self.my_piece == "o":
        opponent_piece = "x"
    else:
        pass

    for i in range(0, 3):
        for j in range(0, 3):
            if board1[i][j] == "n":
                board1[i][j] = opponent_piece
                if board1[0][0] == board1[0][1] == board1[0][2] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[1][0] == board1[1][1] == board1[1][2] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[2][0] == board1[2][1] == board1[2][2] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[0][0] == board1[1][0] == board1[2][0] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[0][1] == board1[1][1] == board1[2][1] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[0][2] == board1[1][2] == board1[2][2] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[0][0] == board1[1][1] == board1[2][2] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                elif board1[0][2] == board1[1][1] == board1[2][0] == opponent_piece:
                    move.append([i, j])
                    board1[i][j] = "n"
                else:
                    move.append([9, 9])
                    board1[i][j] = "n"
    return move


def potential_win(self, board):
    board1 = deepcopy(board)

    for i in range(0, 3):
        for j in range(0, 3):
            if board1[i][j] == "n":
                board1[i][j] = self.my_piece
                if board1[0][0] == board1[0][1] == board1[0][2] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[1][0] == board1[1][1] == board1[1][2] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[2][0] == board1[2][1] == board1[2][2] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[0][0] == board1[1][0] == board1[2][0] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[0][1] == board1[1][1] == board1[2][1] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[0][2] == board1[1][2] == board1[2][2] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[0][0] == board1[1][1] == board1[2][2] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                elif board1[0][2] == board1[1][1] == board1[2][0] == self.my_piece:
                    row_num = i
                    col_num = j
                    return row_num, col_num
                else:
                    return "no win"


def random_move(self, board):
    board1 = deepcopy(board)
    potential_move = [[]]

    for i in range(0, 3):
        for j in range(0, 3):
            if board1[i][j] == "n":
                potential_move.append([i, j])

    return potential_move[1]
