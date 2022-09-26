'''
The module that runs the program
'''
from players import ComputerPlayer, UserPlayer
from visuals import messages, cb, yb, bb


class TicTacToe:
    '''
    The tic tac toe game
    '''

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.columns = 3
        self.rows = 3
        self.winner = None
        self.current_letter = messages['x-letter']
        self. available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_board(self):
        '''
        Print the tic tac toe game board
        '''
        for row in range(self.rows):
            print(messages['board-line'])
            print(messages['side-line'], end='')
            for column in range(self.columns):
                print('', self.board[row][column], end=f' {messages["side-line"]}')
        print(messages['board-line'])

    def available_moves(self):
        '''
        Returns all the available squares that the player can make a move on
        '''
        moves = []

        for row in range(3):
            for column in range(3):
                moves.append(self.board[row][column])
        return moves

    def append_move_to_board(self, move):
        '''
        Add the player move to the board if it is a valid move
        Remove the square from the avaible moves
        '''
        # turn = [messages['x-letter'] if self.current_letter == messages['x-letter'] else messages['x-letter']]

        if move >= 1 and move <= 3:
            self.board[0][move-1] = self.current_letter
        elif move >= 4 and move <= 6:
            self.board[1][move-4] = self.current_letter
        elif move >= 7 and move <= 9:
            self.board[2][move-7] = self.current_letter
        del self.available_moves()[move - 1]

        # print(f'{self.current_letter} has moved to square {move}\n')
        # print(f"It is {turn[0]}'s turn")

    def check_for_win(self):
        '''
        Check if the player has won:
        - horizontally
        - vertically
        - Diagonally
        '''
        global game_running
        # self.winner = None
        vertical_win_row = [[], [], []]
        diagonal_win = [[], [], []]
        j = 2

        for i in range(3):
            diagonal_win[0].append(self.board[i][i])
            diagonal_win[1].append(self.board[j][i])
            j = j - 1
            for k in range(3):
                vertical_win_row[i].append(self.board[k][i])

        for i in range(3):
            # Check for horizontal win
            if self.board[i].count(self.current_letter) == 3:
                self.winner = self.current_letter
                break
            # Check for vertical win
            elif vertical_win_row[i].count(self.current_letter) == 3:
                self.winner = self.current_letter
                break
            # Check for diagonal win
            elif diagonal_win[i].count(self.current_letter) == 3:
                self.winner = self.current_letter
                break

        if self.winner != None:
            background = cb if self.winner == messages['x-letter'] else yb
            self.print_board()
            print(f'{background}\n{self.winner} has won!{bb}')
            self.play_again()

    def change_player(self):
        '''
        switch players
        '''
        if self.current_letter == messages['x-letter']:
            self.current_letter = messages['o-letter']
        else:
            self.current_letter = messages['x-letter']

    def check_for_tie(self):
        global game_running
        if (' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]) and not self.check_for_win():
            print('It is a tie!')
            game_running = False


    def play_again(self):
        '''
        Checks if the user wants to play again and
        resets the game board if the answer is yes or
        exits the game if the answer is no
        '''
        global game_running
        is_answer_valid = False
        while is_answer_valid == False:
            answer = input('Do you want to play again? (yes/no): ').lower()
            if answer == 'yes':
                is_answer_valid = True
                game_running = True
                for i in range(3):
                    for j in range(3):
                        self.board[i][j] = ' '
                self.available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            elif answer == 'no':
                is_answer_valid = True
                game_running = False
            else:
                is_answer_valid = False
                print('Please enter "yes" or "no"')


game_running = True


def main():
    # Print the welcome header
    print(messages['welcome'])
    print(messages['TTT'])

    # Start the game
    t = TicTacToe()
    while (' ' in t.board[0] or ' ' in t.board[1] or ' ' in t.board[2]) and game_running:
        t.print_board()
        moves = t.available_moves()
        user_move = UserPlayer().get_valid_user_move(moves, t)
        t.append_move_to_board(user_move)
        t.check_for_win()
        if t.winner != None:
            t.winner = None
            continue
        t.change_player()
        cpu_move = ComputerPlayer().get_valid_computer_move(t)
        try:
            t.append_move_to_board(cpu_move)
        except TypeError:
            print()  # This is for when all squares are taken and X makes the last move
        t.check_for_win()
        t.change_player()


main()
