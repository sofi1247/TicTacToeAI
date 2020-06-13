from abc import ABC, abstractmethod


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