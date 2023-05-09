import time
class BoardClass:

    def __init__(self, user, last_user, num_wins, num_ties, num_losses):
        self.entire_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_player = 'x' 
        self.games_played = 0
        self.user = user
        self.last_user = ''
        self.num_wins = 0
        self.num_ties = 0
        self.num_losses = 0

    def entireList(self):
        return self.entire_list

    def emptyList(self):
        self.entire_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        return self.entire_list

    def numWins(self):
        self.num_wins += 1
        return self.num_wins

    def numTies(self):
        self.num_ties += 1
        return self.num_ties

    def numLosses(self):
        self.num_losses += 1
        return self.num_losses
    
    def updateGamesPlayed(self):
        self.games_played += 1
        return self.games_played
    
    def resetGameBoard(self):
        self.entire_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        line = 0
        for row in self.entire_list:
            string = f'{row[0]} | {row[1]} | {row[2]}'
            line += 1
            if line <= 2:
                print(string)
                print('- + - + -')
            else:
                print(string)

    def checkSpace(self, x):
        if 1 <= x <= 3:
            if self.entire_list[0][x-1] == ' ':
                return True
        elif 4 <= x <= 6:
            if self.entire_list[1][x-4] == ' ':
                return True
        elif 7 <= x <= 9:
            if self.entire_list[2][x-7] == ' ':
                return True
        

    def updateGameBoard(self, x):
        if self.current_player == 'o':
            player_symbol = 'o'
            self.current_player = 'x'
        else:
            player_symbol = 'x'
            self.current_player = 'o'
            
        if 1 <= x <= 3:
            self.entire_list[0][x-1] = player_symbol
        elif 4 <= x <= 6:
            self.entire_list[1][x-4] = player_symbol
        elif 7 <= x <= 9:
            self.entire_list[2][x-7] = player_symbol

        line = 0 
        for row in self.entire_list:
            line += 1
            string = f'{row[0]} | {row[1]} | {row[2]}'
            if line <= 2:
                print(string)
                print('- + - + -')
            else:
                print(string)
            
    def isWinner(self):
        for i in range(3):
            if self.entire_list[i][0] == self.entire_list[i][1] == self.entire_list[i][2] and self.entire_list[i][0] != ' ':
                return True
            elif self.entire_list[0][i] == self.entire_list[1][i] == self.entire_list[2][i] and self.entire_list[0][i] != ' ':
                return True
        if self.entire_list[0][0] == self.entire_list[1][1] == self.entire_list[2][2] and self.entire_list[0][0] != ' ':
            return True
        elif self.entire_list[0][2] == self.entire_list[1][1] == self.entire_list[2][0] and self.entire_list[0][2] != ' ':
            return True
        else:
            return False

    def boardIsFull(self):
        for row in self.entire_list:
            for element in row:
                if element == ' ':
                    return False
        return True

    def printStats(self):
        if self.current_player == 'o':
            self.last_user = 'x'
        elif self.current_player == 'x':
            self.last_user = 'o'
        print('Username:', self.user)
        print('Last move by:', self.last_user)
        print('Number of games:', self.games_played)
        print('Number of wins:', self.num_wins)
        print('Nunber of losses:', self.num_losses)
        print('Number of ties:', self.num_ties)


    def oppositeUser(self):
        if self.current_player == 'o':
            self.last_user = 'x'
            return self.last_user
        elif self.current_player == 'x':
            self.last_user = 'o'
            return self.last_user
    


if __name__ == '__main__':
    user = input('Username: ')
    game_board = BoardClass(user, last_user='', num_wins=0, num_ties=0, num_losses=0)
    run = True
    print('Welcome to Taiki\'s Tic-Tac-Toe!')
    #time.sleep(1)
    print('The number assigned to each box on the board looks like this...')
    #time.sleep(1)
    print('1 | 2 | 3')
    print('- + - + -')
    print('4 | 5 | 6')
    print('- + - + -')
    print('7 | 8 | 9')
    #time.sleep(2)
    while run:
        x = input(f"{game_board.current_player}'s turn. Please enter an integer value of 1-9: ")
        if x.isdigit():
            x = int(x)
            if 1 <= x <= 9:
                if game_board.checkSpace(x) == True:
                    game_board.updateGameBoard(x)
                    if game_board.isWinner():
                        num = game_board.updateGamesPlayed()
                        print(f'{game_board.oppositeUser()} wins')
                        if game_board.current_player == 'o': #change this to the user later, x should be player 1
                            game_board.numWins()
                        else:
                            game_board.numLosses()
                        answer = True
                        while answer:
                            y = input('Would you like to play another game?')
                            if y == 'y' or y == 'Y':
                                print('Play Again')
                                answer = False
                                game_board.emptyList()
                            elif y == 'n' or y == 'N':
                                print('Fun Times')
                                game_board.printStats()
                                run = False
                                answer = False
                            else:
                                print('Options: \'y\' or \'Y\' and \'n\' or \'N\'')
                                answer = True
                                        
                    elif game_board.boardIsFull():
                        game_board.numTies()
                        print('Full Board')
                        answer = True
                        while answer:
                            y = input('Would you like to play another game?')
                            if y == 'y' or y == 'Y':
                                print('Play Again')
                                answer = False
                                game_board.emptyList()
                            elif y == 'n' or y == 'N':
                                print('Fun Times')
                                game_board.printStats()
                                run = False
                                answer = False
                            else:
                                print('Options: \'y\' or \'Y\' and \'n\' or \'N\'')
                                answer = True

                else:
                    print('That spot is already taken. Please choose a different spot.')
            else:
                print('Integer is not between 1-9.')
        elif x == 'r':
            game_board.resetGameBoard()
            num = game_board.updateGamesPlayed()
        elif x == 'p':
            game_board.printStats()
        else:
            print('You did not provide an integer.')
