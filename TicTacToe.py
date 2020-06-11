class TicTacToe:

    def __init__(self, player1, player2):
        self.turn_counter = 0
        self.curr_player = player1
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0
        self.score_draw = 0
        self.piece_x = "x"
        self.piece_o = "o"
        self.board = [["n", "n", "n"], ["n", "n", "n"], ["n", "n", "n"]]

    def reset_game(self):
        self.turn_counter = 0
        self.board = [["n", "n", "n"], ["n", "n", "n"], ["n", "n", "n"]]
        self.curr_player = self.player1

    def print_state(self):
        print("Turn: " + str(self.turn_counter))
        print("Whose turn: " + self.curr_player)

        for i in range(0,3):
            for j in range(0,3):
                print(self.board[i][j], end=" ")

            print()

    def game_loop(self):
        row_num = int(input("Row number: "))
        col_num = int(input("Column number: "))

        if self.board[row_num][col_num] == "n":
            if self.curr_player == self.player1:
                self.board[row_num][col_num] = "x"
                self.curr_player = self.player2
            else:
                self.board[row_num][col_num] = "o"
                self.curr_player = self.player1
        else:
            print("This tile is already filled. Please choose another one.")

        self.turn_counter += 1
        self.win_check()

        if self.win_check() == "continue":
            self.print_state()
            self.game_loop()
        else:
            self.print_state()
            print("The winner is " + self.win_check())

    def win_check(self):
        # checking first row
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != "n":
            win_piece = self.board[0][0]
        # checking second row
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != "n":
            win_piece = self.board[1][0]
        # checking third row
        elif self.board[2][0] == self.board[0][1] == self.board[0][2] and self.board[2][0] != "n":
            win_piece = self.board[2][0]
        # checking first column
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != "n":
            win_piece = self.board[0][0]
        # checking second column
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != "n":
            win_piece = self.board[0][1]
        # checking third column
        elif self.board[0][2] == self.board[2][1] == self.board[2][2] and self.board[0][2] != "n":
            win_piece = self.board[0][2]
        # checking left diagonal
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "n":
            win_piece = self.board[0][0]
        # checking right diagonal
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != "n":
            win_piece = self.board[1][1]
        else:
            return "continue"

        if win_piece == "x":
            return self.player1
        elif win_piece == "o":
            return self.player2




    def board_test(self):
        self.board = [["n", "n", "n"], ["n", "x", "n"], ["n", "x", "n"]]

    def print_score(self):
        pass