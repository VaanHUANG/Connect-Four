from Player import player


class human(player):
    def next_column(self, game_board):
        # ask for input
        # check valid
        while(True):
            user_input = raw_input("Your move: ")
            if user_input in ["1", "2", "3", "4", "5", "6", "7"]:
                break
            print "Invalid input!"
        # update game board

        for i in range(6):
            if i == 5 and game_board[i][int(user_input) - 1] == " ":
                game_board[5][int(user_input) - 1] = self.player_symbol
                break
            elif i > 0 and game_board[i][int(user_input) - 1] != " ":
                game_board[i - 1][int(user_input) - 1] = self.player_symbol
                break
            elif i == 0 and game_board[i][int(user_input) - 1] != " ":
                print "This column is full! Try another!"
                self.next_column(game_board)
                break
        # return next choice
        return input