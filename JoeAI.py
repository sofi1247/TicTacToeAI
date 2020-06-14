import Player
import random

class JoeAI(Player.Player):

    def __init__(self, piece, difficulty):
        self.piece = piece
        self.last_move = None
        self.offense = None
        self.distance = 0
        if piece == 'x':
            self.opponents_piece = 'o'
        else:
            self.opponents_piece = 'x'
        self.turn = 0
        if 1 <= difficulty <= 3:
            self.difficulty = difficulty
        else:
            raise ValueError("Invalid difficulty level. This AI accepts difficulties between 1 and 3")
        self.name = "JoeAI-" + str(difficulty)

    def make_move(self, board):

        # Strategy 1: Make random moves
        if self.difficulty == 1:
            return self.make_random_move(board)

        # Strategy 2: Make moves adjacent to current pieces, win when possible, otherwise random
        elif self.difficulty == 2:
            winning_move = self.has_winning_move(board, self.piece)
            if winning_move is not None:
                return winning_move
            elif self.last_move is not None:
                options = self.get_adjacent_positions(board, self.last_move)
                if len(options) == 0:
                    row, col = self.make_random_move(board)
                    self.last_move = (row, col)
                    return row, col
                else:
                    row, col = options[random.randint(0, len(options) - 1)]
            else:
                row, col = self.make_random_move(board)

            self.last_move = (row, col)
            print(row, col)
            return row, col

        # Strategy 3: On offense, refer to turn based strat
        else:
            self.turn += 1
            if self.offense is None:
                self.offense = self.is_going_first(board)

            if self.turn > 1:
                winning_move = self.has_winning_move(board, self.piece)
                if winning_move is not None:
                    return winning_move


                opponent_winning_move = self.has_winning_move(board, self.opponents_piece)
                if opponent_winning_move is not None:
                    return opponent_winning_move

            if self.offense:
                # On turn one pick a random corner
                if self.turn == 1:
                    options = [(0,0), (0,2), (2,0), (2,2)]
                    self.last_move = options[random.randint(0, len(options) - 1)]

                # On turn two, get distance from us that opponent played and play optimal strategy
                elif self.turn == 2:
                    opps_move = self.find_opponents_piece(board)
                    self.distance = abs(self.last_move[0] - opps_move[0]) + abs(self.last_move[1] - opps_move[1])

                    if self.distance == 1:  # Play adjacent corner not block by opponents move
                        options = self.get_vacant_corners(board)
                        print(self.last_move)
                        for option in options:
                            print(option)
                            dist = abs(option[0] - self.last_move[0]) + abs(option[1] - self.last_move[1])
                            print(dist)
                            if dist != 4 and len(self.get_adjacent_positions(board, option)) == 2:
                                self.last_move = option
                                break

                    elif self.distance == 2:  # Play opposite corner
                        self.last_move = (2 - self.last_move[0], 2 - self.last_move[1])

                    elif self.distance == 3:  # Play corner non adjacent to opponents move
                        options = self.get_vacant_corners(board)
                        best_option = options[0]
                        option_dist = -1
                        for option in options:
                            dist = abs(option[0] - opps_move[0]) + abs(option[1] - opps_move[1])
                            if dist > option_dist:
                                best_option = option
                                option_dist = dist
                        self.last_move = best_option

                    else:  # Play non opposite corner
                        options = self.get_vacant_corners(board)
                        self.last_move = options[random.randint(0, len(options) - 1)]

                # On turn three, depending on our turn two play we force a win or draw
                elif self.turn == 3:
                    # In case one or three we play center to force a win
                    if self.distance == 1 or self.distance == 3:
                        self.last_move = (1,1)

                    # In the only other case (case 4) we play the remaining corner to force a win
                    else:
                        self.last_move = self.get_vacant_corners(board)[0]

            else:
                if self.turn == 1:
                    if self.is_spot_vacant(board, (1,1)):
                        self.last_move = (1,1)
                    else:
                        options = self.get_vacant_corners(board)
                        self.last_move = options[random.randint(0, len(options) - 1)]
                elif self.turn == 2:
                    options = self.get_adjacent_positions(board, self.last_move)
                    self.last_move = options[random.randint(0, len(options) - 1)]
                else:
                    self.last_move = self.make_random_move(board)

            return self.last_move


    def is_spot_vacant(self, board, position):
        return board[position[0]][position[1]] == 'n'

    def get_vacant_corners(self, board):
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        options = []

        for corner in corners:
            if board[corner[0]][corner[1]] == 'n':
                options.append(corner)

        return options

    def find_opponents_piece(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == self.opponents_piece:
                    return (row, col)

    def is_going_first(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != "n":
                    return False

        return True

    def get_adjacent_positions(self, board, move):
        options = []
        if move[0] - 1 > 0 and board[move[0] - 1][move[1]] == "n":
            options.append((move[0] - 1, move[1]))
        if move[0] + 1 < len(board) and board[move[0] + 1][move[1]] == "n":
            options.append((move[0] + 1, move[1]))
        if move[1] - 1 > 0 and board[move[0]][move[1] - 1] == "n":
            options.append((move[0], move[1] - 1))
        if move[1] + 1 < len(board[0]) and board[move[0]][move[1] + 1] == "n":
            options.append((move[0], move[1] + 1))
        return options

    def make_random_move(self, board):
        options = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "n":
                    options.append((row, col))

        return options[random.randint(0, len(options) - 1)]

    def has_winning_move(self, board, piece):
        if self.count_matches(board, piece, [(0,0), (0,1), (0,2)]) == 2:
            return self.find_odd_one_out(board, piece, [(0,0), (0,1), (0,2)])
        elif self.count_matches(board, piece, [(1,0), (1,1), (1,2)]) == 2:
            return self.find_odd_one_out(board, piece, [(1,0), (1,1), (1,2)])
        elif self.count_matches(board, piece, [(2,0), (2,1), (2,2)]) == 2:
            return self.find_odd_one_out(board, piece, [(2,0), (2,1), (2,2)])
        elif self.count_matches(board, piece, [(0,0), (1,0), (2,0)]) == 2:
            return self.find_odd_one_out(board, piece, [(0,0), (1,0), (2,0)])
        elif self.count_matches(board, piece, [(0,1), (1,1), (2,1)]) == 2:
            return self.find_odd_one_out(board, piece, [(0,1), (1,1), (2,1)])
        elif self.count_matches(board, piece, [(0,2), (1,2), (2,2)]) == 2:
            return self.find_odd_one_out(board, piece, [(0,2), (1,2), (2,2)])
        elif self.count_matches(board, piece, [(0,0), (1,1), (2,2)]) == 2:
            return self.find_odd_one_out(board, piece, [(0,0), (1,1), (2,2)])
        elif self.count_matches(board, piece, [(0,2), (1,1), (2,0)]) == 2:
            return self.find_odd_one_out(board, piece, [(0,2), (1,1), (2,0)])
        else:
            return None

    def count_matches(self, board, piece, positions):
        count = 0
        for position in positions:
            if board[position[0]][position[1]] == piece:
                count += 1
            elif board[position[0]][position[1]] != "n":
                return -1
        return count

    def find_odd_one_out(self, board, piece, positions):
        for position in positions:
            if board[position[0]][position[1]] != piece:
                return position[0], position[1]
