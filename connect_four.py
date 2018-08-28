import sys
import abc
import os
import random
'''
CSCI3180 Principles of Programming Languages
--- Declaration ---
I declare that the assignment here submitted is original except for source
material explicitly acknowledged. I also acknowledge that I am aware of
University policy and regulations on honesty in academic work, and of the
disciplinary guidelines and procedures applicable to breaches of such policy
 and regulations, as contained in the website
 http://www.cuhk.edu.hk/policy/academichonesty
Assignment 2
Name : Tseng,Po-Cheng
Student ID : 1155071386
Email Address : pctseng6@cse.cuhk.edu.hk
'''
width = 6
length = 7
class ConnectFour(object):
    highlight_pos = []
    current_player = None
    def __init__(self):
        self.turn = 1
        self.winner = None
        self.game_board=[]
        self.complete = None
        self.no= 0
        for _row in range(width):
            new =[]
            for _col in range(length):
                new.append('0')
            self.game_board.append(new)
    def start_game(self):
        choice1 = None
        while choice1==None:
            print("Please choose the first player:")
            print("1.Computer")
            print("2.Human")
            try:
                choice1 = int(raw_input("Your choice is:"))
            except ValueError:
                choice1 = None
            if choice1 == 1:
                print("Player O is Computer")
                self.player1 = Computer("O") # The first player is a computer
                break
            elif choice1 == 2:
                print("Player O is Human")
                self.player2 = Human("O") # The first player is a human
                break
            else:
                choice1= None
                print("Invalid number!! Please insert either 1 or 2")
        choice2 = None
        while choice2== None:
            print("Please choose the second player:")
            print("1.Computer")
            print("2.Human")
            try:
                choice2=int(raw_input("Your choice is:"))
            except ValueError:
                choice2 = None
            if choice2==1 or choice2==2:
                if choice2 == 1:
                    print("Player X is Computer")
                    self.player1 = Computer("X") # The second player is a computer
                    break
                elif choice2 == 2:
                    print("Player X is Human")
                    self.player2 = Human("X") # The second player is a human
                    break
            else:
                choice2 = None
                print("Invalid number!! Please insert either 1 or 2")
            # the game starts with the 'O' player
            self.current_player = 'O'
            while not self.complete:
                self.next_turn()
    def change_player(self):
        if self.current_player == 'O':
            self.current_player = 'X'
        elif self.current_player == 'X':
            self.current_player = 'O'
    def is_filled_col(self,col):
        for i in range(width):
            if self.game_board[i][col]=='O' or self.game_board[i][col]== 'X':
                continue
            elif self.game_board[i][col]=='0':
                return False
        return True
    def next_turn(self):
            # to get the next column from the input given by player
            column = self.current_player.next_column(self.game_board)
            # checking if the column is filled
            for i in range(width-1,-1,-1):
                if  self.game_board[i][column]== '0':
                    self.game_board[i][column] = self.current_player
                    self.check_finished()
                    self.print_message()
                    self.print_board_game()
                    # changing player
                    self.change_player()
                if self.turn == width*length:
                    print("  Draw Game!!!")
                self.turn +=1
                if self.is_full() and self.is_four==False:
                    print("  It is a draw!!!")
            # the given column is full
            print("Column %d is already full. Please insert another column"%(column+1))
            return
    # the number of 'O' and 'X' in the game_board will not be equal or larger than height* weight unless the board is full
    def is_full(self):
        return self.turn >width*length # 42 in this case
    def check_finished(self):
        if self.is_four():
            self.complete = True
            self.winner= self.current_player
        elif self.is_full():
            self.complete = True
    def check_vertical_four(self,row,col):
        #check for the vertical direction
        count = 0
        if row+ 3 < width and col<length:
            for i in range(4):
                if self.game_board[row][col]== self.game_board[row+i][col]:
                    count +=1
            if count==4:
                for i in range(4):
                    self.highlight_pos.append([row+i,col])
                    # Storing the highlighted positions into the list
                    return True
    def check_horizontal_four(self,row,col):
        #check for the horizontal direction
        count = 0
        if row< width and col+3 <length:
            for i in range(4):
                if self.game_board[row][col]== self.game_board[row][col+i]:
                    count +=1
            if count ==4:
                for i in range(4):
                    self.highlight_pos.append([row,col+i])
                    #Storing the highlighted positions into the list
                return True
    def check_right_diagonal_four(self,row,col):
        #check for the diagonal with positive slope
        count = 0
        if row >=3 and col+3<length:
            for i in range(4):
                if self.game_board[row][col]== self.game_board[row-i][col+i]:
                    count+=1
                if count == 4:
                    for i in range(4):
                        self.highlight_pos.append([row-i,col+i])
                        #Storing the highlighted positions into the list
                    return True
    def check_left_diagonal_four(self,row,col):
        #check for the diagonal with negative slope
        count = 0
        if row>=3 and col>= 3:
            for i in range(4):
                if self.game_board[row][col]== self.game_board[row+i][col+i]:
                    count+=1
                if count == 4:
                    for i in range(4):
                        self.highlight_pos.append([row+i,col+i])
                        # Storing the highlighted positions into the list
                    return True
    def print_message(self):
        print("Round:        "+self.turn)
        if self.complete:
            pass

    def is_four(self):
        for i in width:
            for j in length:
                if self.check_horizontal_four(i,j) or self.check_right_diagonal_four(i,j) or self.check_left_diagonal_four(i,j) or self.check_vertical_four(i,j):
                    # Preventing repetitions in the list
                    self.highlight_pos= list(set(self.highlight_pos))
                    return True
        return False
# choices are the numbers given from the command line
# using commas without adding newlines
    def print_board_game(self):
        for i in range(1,length+1):
            print ("| %d" %i),
        print("|")
        print('-'*30)
        for _row in range(width):
            for _col in range(length):
                if(self.game_board[_row][_col]=='0'):
                    print("|  "),
                elif(self.game_board[_row][_col]=='O'):
                    print("| O "),
                elif(self.game_board[_row][_col]=='X'):
                    print("| X "),
            print("|")
            print("-"*30)
class Player(object):
    name = None
    def __init__(self,player_symbol):
        __metaclass__=abc.ABCMeta
        @abc.abstractmethod
        def next_column(self,game_board, player_symbol):
            return
class Human(Player):
    def __init__(self,player_symbol):
        super.__init__(self,player_symbol)
        self.name = "Human"
    def next_column(self,game_board):
        while True:
            try:
                column = (int)(raw_input("Please enter an integer between 1 and 7:")) - 1
            except ValueError:
                pass
            if column>=0 and column<=6:
                return column
            else:
                print("Please enter an integer between 1 and 7 once again.")
class Computer(Player):
    def __init__(self,player_symbol):
        super.__init__(self,player_symbol)
        self.name = "Computer"
    def next_column(self,game_board):
        while True:
            try:
                column= random.randint(0,6)
            except ValueError:
                pass
            if column>=0 and column<=6:
                return column
            else:
                pass
connect_four = ConnectFour()
connect_four.print_board_game()
connect_four.start_game()
