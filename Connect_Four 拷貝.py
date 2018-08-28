from Computer import computer
from Human import  human


class Connect_Four(object):
    @property
    def gameBoard(self):
        return self._gameBoard

    @gameBoard.setter
    def gameBoard(self, gameBoard):
        self._gameBoard = gameBoard

    @property
    def player_O(self):
        return self._player_O

    @player_O.setter
    def player_O(self, player_O):
        self._player_O = player_O

    @property
    def player_X(self):
        return self._player_X

    @player_X.setter
    def player_X(self, player_X):
        self._player_X = player_X

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        self._turn = turn

    # Above are four instance variables, for gameBoard, still need to check how to initialize a list
    def __init__(self):
        self._player_O = "O"
        self._player_X = "X"
        self._turn = "O"
        self.start_game()

    def start_game(self):
        choice_1 = 0
        while (choice_1 != "1" and choice_1 != "2"):
            print "Please choose the first player:"
            print "1.Computer"
            print "2.Human"
            choice_1 = raw_input("Your choice is: ")
            if (choice_1 == "1" or choice_1 == "2"):
                if choice_1 == "1":
                    print "Player O is Computer"
                    self.player_O = "C"
                else:
                    print "Player O is Human"
                    self.player_O = "H"
        while (True):
            print "Please choose the second player:"
            print "1.Computer"
            print "2.Human"
            choice_2 = raw_input("Your choice is: ")
            if choice_2 == "1" or choice_2 == "2":
                if choice_2 == "1":
                    print "Player X is Computer"
                    self.player_X = "C"
                else:
                    print "Player X is Human"
                    self.player_X = "H"
                break
        return None

    def print_game_board(self, game_board):
        print "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |"
        print "-----------------------------"
        for i in range(6):
            for j in range(7):
                if game_board[i][j] == "IO":
                    print "|\033[7m O\033[m",
                elif game_board[i][j] == "IX":
                    print "|\033[7m X\033[m",
                else:
                    print "| %c" % game_board[i][j],
            print "|"
            print "-----------------------------"
        return None


    def switch(self, current_player_symbol):
        if current_player_symbol == "O":
            current_player = playerX
        if current_player_symbol == "X":
            current_player = playerO

    # Above are instance methods
    def is_end(self, game_board):
        while(True):
            # see whether "O" wins
            for i in range(6):
                for j in range(7):
                    if game_board[i][j] == "O" or game_board[i][j] == "IO":
                        if j + 1 < 7 and (game_board[i][j + 1] == "O" or game_board[i][j + 1] == "IO"):
                            if j + 2 < 7 and (game_board[i][j + 2] == "O" or game_board[i][j + 2] == "IO"):
                                if j + 3 < 7 and (game_board[i][j + 3] == "O" or game_board[i][j + 3] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i][j + 1] = "IO"
                                    game_board[i][j + 2] = "IO"
                                    game_board[i][j + 3] = "IO"
                                    return "O"
                        if j - 1 >= 0 and (game_board[i][j - 1] == "O" or game_board[i][j - 1] == "IO"):
                            if j - 2 >= 0 and (game_board[i][j - 2] == "O" or game_board[i][j - 2] == "IO"):
                                if j - 3 >= 0 and (game_board[i][j - 3] == "O" or game_board[i][j - 3] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i][j - 1] = "IO"
                                    game_board[i][j - 2] = "IO"
                                    game_board[i][j - 3] = "IO"
                                    return "O"
                        if i - 1 >= 0 and (game_board[i - 1][j] == "O" or game_board[i - 1][j] == "IO"):
                            if i - 2 >= 0 and (game_board[i - 2][j] == "O" or game_board[i - 2][j] == "IO"):
                                if i - 3 >= 0 and (game_board[i - 3][j] == "O" or game_board[i - 3][j] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i - 1][j] = "IO"
                                    game_board[i - 2][j] = "IO"
                                    game_board[i - 3][j] = "IO"
                                    return "O"
                        if i + 1 < 6 and (game_board[i + 1][j] == "O" or game_board[i + 1][j] == "IO"):
                            if i + 2 < 6 and (game_board[i + 2][j] == "O" or game_board[i + 2][j] == "IO"):
                                if i + 3 < 6 and (game_board[i + 3][j] == "O" or game_board[i + 3][j] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i + 1][j] = "IO"
                                    game_board[i + 2][j] = "IO"
                                    game_board[i + 3][j] = "IO"
                                    return "O"
                        if i - 1 >= 0 and j + 1 < 7 and (game_board[i - 1][j + 1] == "O" or game_board[i - 1][j + 1] == "IO"):
                            if i - 2 >= 0 and j + 2 < 7 and (game_board[i - 2][j + 2] == "O" or game_board[i - 2][j + 2] == "IO"):
                                if i - 3 >= 0 and j + 3 < 7 and (game_board[i - 3][j + 3] == "O" or game_board[i - 3][j + 3] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i - 1][j + 1] = "IO"
                                    game_board[i - 2][j + 2] = "IO"
                                    game_board[i - 3][j + 3] = "IO"
                                    return "O"
                        if i + 1 < 6 and j + 1 < 7 and (game_board[i + 1][j + 1] == "O" or game_board[i + 1][j + 1] == "IO"):
                            if i + 2 < 6 and j + 2 < 7 and (game_board[i + 2][j + 2] == "O" or game_board[i + 2][j + 2] == "IO"):
                                if i + 3 < 6 and j + 3 < 7 and (game_board[i + 3][j + 3] == "O" or game_board[i + 3][j + 3] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i + 1][j + 1] = "IO"
                                    game_board[i + 2][j + 2] = "IO"
                                    game_board[i + 3][j + 3] = "IO"
                                    return "O"
                        if i + 1 < 6 and j - 1 >= 0 and (game_board[i + 1][j - 1] == "O" or game_board[i + 1][j - 1] == "IO"):
                            if i + 2 < 6 and j - 2 >= 0 and (game_board[i + 2][j - 2] == "O" or game_board[i + 2][j - 2] == "IO"):
                                if i + 3 < 6 and j - 3 >= 0 and (game_board[i + 3][j - 3] == "O" or game_board[i + 3][j - 3] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i + 1][j - 1] = "IO"
                                    game_board[i + 2][j - 2] = "IO"
                                    game_board[i + 3][j - 3] = "IO"
                                    return "O"
                        if i - 1 >= 0 and j - 1 >= 0 and (game_board[i - 1][j - 1] == "O" or game_board[i - 1][j - 1] == "IO"):
                            if i - 2 >= 0 and j - 2 >= 0 and (game_board[i - 2][j - 2] == "O" or game_board[i - 2][j - 2] == "IO"):
                                if i - 3 >= 0 and j - 3 >= 0 and (game_board[i - 3][j - 3] == "O" or game_board[i - 3][j - 3] == "IO"):
                                    game_board[i][j] = "IO"
                                    game_board[i][j + 1] = "IO"
                                    game_board[i][j + 2] = "IO"
                                    game_board[i][j + 3] = "IO"
                                    return "O"
            # see whether "X" wins
            for i in range(6):
                for j in range(7):
                    if game_board[i][j] == "X" or game_board[i][j] == "IX":
                        if j + 1 < 7 and (game_board[i][j + 1] == "X" or game_board[i][j + 1] == "IX"):
                            if j + 2 < 7 and (game_board[i][j + 2] == "X" or game_board[i][j + 2] == "IX"):
                                if j + 3 < 7 and (game_board[i][j + 3] == "X" or game_board[i][j + 2] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i][j + 1] = "IX"
                                    game_board[i][j + 2] = "IX"
                                    game_board[i][j + 3] = "IX"
                                    return "X"
                        if j - 1 >= 0 and (game_board[i][j - 1] == "X" or game_board[i][j - 1] == "IX"):
                            if j - 2 >= 0 and (game_board[i][j - 2] == "X" or game_board[i][j - 2] == "IX"):
                                if j - 3 >= 0 and (game_board[i][j - 3] == "X" or game_board[i][j - 3] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i][j - 1] = "IX"
                                    game_board[i][j - 2] = "IX"
                                    game_board[i][j - 3] = "IX"
                                    return "X"
                        if i - 1 >= 0 and (game_board[i - 1][j] == "X" or game_board[i - 1][j] == "IX"):
                            if i - 2 >= 0 and (game_board[i - 2][j] == "X" or game_board[i - 2][j] == "IX"):
                                if i - 3 >= 0 and (game_board[i - 3][j] == "X" or game_board[i - 3][j] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i - 1][j] = "IX"
                                    game_board[i - 2][j] = "IX"
                                    game_board[i - 3][j] = "IX"
                                    return "X"
                        if i + 1 < 6 and (game_board[i + 1][j] == "X" or game_board[i + 1][j] == "IX"):
                            if i + 2 < 6 and (game_board[i + 2][j] == "X" or game_board[i + 2][j] == "IX"):
                                if i + 3 < 6 and (game_board[i + 3][j] == "X" or game_board[i + 3][j] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i + 1][j] = "IX"
                                    game_board[i + 2][j] = "IX"
                                    game_board[i + 3][j] = "IX"
                                    return "X"
                        if i - 1 >= 0 and j + 1 < 7 and (game_board[i - 1][j + 1] == "X" or game_board[i - 1][j + 1] == "IX"):
                            if i - 2 >= 0 and j + 2 < 7 and (game_board[i - 2][j + 2] == "X" or game_board[i - 2][j + 2] == "IX"):
                                if i - 3 >= 0 and j + 3 < 7 and (game_board[i - 3][j + 3] == "X" or game_board[i - 3][j + 3] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i - 1][j + 1] = "IX"
                                    game_board[i - 2][j + 2] = "IX"
                                    game_board[i - 3][j + 3] = "IX"
                                    return "X"
                        if i + 1 < 6 and j + 1 < 7 and (game_board[i + 1][j + 1] == "X" or game_board[i + 1][j + 1] == "IX"):
                            if i + 2 < 6 and j + 2 < 7 and (game_board[i + 2][j + 2] == "X" or game_board[i + 2][j + 2] == "IX"):
                                if i + 3 < 6 and j + 3 < 7 and (game_board[i + 3][j + 3] == "X" or game_board[i + 3][j + 3] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i + 1][j + 1] = "IX"
                                    game_board[i + 2][j + 2] = "IX"
                                    game_board[i + 3][j + 3] = "IX"
                                    return "X"
                        if i + 1 < 6 and j - 1 >= 0 and (game_board[i + 1][j - 1] == "X" or game_board[i + 1][j - 1] == "IX"):
                            if i + 2 < 6 and j - 2 >= 0 and (game_board[i + 2][j - 2] == "X" or game_board[i + 2][j - 2] == "IX"):
                                if i + 3 < 6 and j - 3 >= 0 and (game_board[i + 3][j - 3] == "X" or game_board[i + 3][j - 3] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i + 1][j - 1] = "IX"
                                    game_board[i + 2][j - 2] = "IX"
                                    game_board[i + 3][j - 3] = "IX"
                                    return "X"
                        if i - 1 >= 0 and j - 1 >= 0 and (game_board[i - 1][j - 1] == "X" or game_board[i - 1][j - 1] == "IX"):
                            if i - 2 >= 0 and j - 2 >= 0 and (game_board[i - 2][j - 2] == "X" or game_board[i - 2][j - 2] == "IX"):
                                if i - 3 >= 0 and j - 3 >= 0 and (game_board[i - 3][j - 3] == "X" or game_board[i - 3][j - 3] == "IX"):
                                    game_board[i][j] = "IX"
                                    game_board[i - 1][j - 1] = "IX"
                                    game_board[i - 2][j - 2] = "IX"
                                    game_board[i - 3][j - 3] = "IX"
                                    return "X"
            is_full = True
            for i in range(6):
                for j in range(7):
                    if game_board[i][j] == " ":
                        is_full = False
                        break
            return is_full

# game starts
new_game = Connect_Four()
# print game board
column_1 = [" ", " ", " ", " ", " ", " ", " "]
column_2 = [" ", " ", " ", " ", " ", " ", " "]
column_3 = [" ", " ", " ", " ", " ", " ", " "]
column_4 = [" ", " ", " ", " ", " ", " ", " "]
column_5 = [" ", " ", " ", " ", " ", " ", " "]
column_6 = [" ", " ", " ", " ", " ", " ", " "]
chess_board = [column_1, column_2, column_3, column_4, column_5, column_6]
new_game.print_game_board(chess_board)
# initialize players
if new_game.player_O == "C":
    playerO = computer("O")
if new_game.player_O == "H":
    playerO = human("O")
if new_game.player_X == "C":
    playerX = computer("X")
if new_game.player_X == "H":
    playerX = human("X")
current_player = "O"
print playerX.player_symbol
print playerO.player_symbol
# TEST! print current_player.player_symbol
# TEST! current_player = new_game.switch(current_player)
# TEST! print current_player.player_symbol

# chess playing starts
while(new_game.is_end(chess_board) == False):
    if current_player == "O":
        playerO.next_column(chess_board)
    else:
        playerX.next_column(chess_board)
    if current_player == "O":
        current_player = "X"
    else:
        current_player = "O"
    new_game.print_game_board(chess_board)
if new_game.is_end(chess_board) == "O":
    new_game.print_game_board(chess_board)
    print "Player O wins!"
if new_game.is_end(chess_board) == "X":
    new_game.print_game_board(chess_board)
    print "Player X wins!"
if new_game.is_end(chess_board) == True:
    print "Draw Game"
