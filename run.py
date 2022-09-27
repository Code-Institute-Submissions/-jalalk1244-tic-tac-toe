'''
The module with the game class and the main function that runs the game
'''
from players import ComputerPlayer, UserPlayer
from visuals import messages, cb, yb, bb, r, w, gb


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
        self.level = None
        self.score = {'x': 0, 'o': 0}

    def print_board(self):
        '''
        Print the tic tac toe game board
        '''
        for row in range(self.rows):
            print(messages['board-line'])
            print(messages['side-line'], end='')
            for column in range(self.columns):
                print('', self.board[row][column],
                      end=f' {messages["side-line"]}')
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
        # Increment the score
        if self.winner == messages['x-letter']:
            self.score['x'] += 1
        elif self.winner == messages['o-letter']:
            self.score['o'] += 1

        # When there is winner
        if self.winner is not None:
            background = cb if self.winner == messages['x-letter'] else yb
            self.print_board()
            print(f'{background}\n {self.winner} has won!{bb}')
            print(f'\n{w}Score:')
            print(f' {messages["x-letter"]} - {self.score["x"]}')
            print(f' {messages["o-letter"]} - {self.score["o"]}')
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
        '''
        Checks if there is a tie
        '''

        flat_board = sum(self.board, [])
        if ' ' not in flat_board and self.winner is None:
            self.print_board()
            print(f'{gb} It is a tie!{bb}')
            print(' Score:')
            print(f' {messages["x-letter"]} - {self.score["x"]}')
            print(f' {messages["o-letter"]} - {self.score["o"]}')
            self.winner = 'draw'
            self.play_again()

    def play_again(self):
        '''
        Checks if the user wants to play again and
        resets the game board if the answer is yes or
        exits the game if the answer is no
        '''
        global GAME_RUNNING
        is_answer_valid = False
        while is_answer_valid is False:
            answer = input('\n Do you want to play again? (yes/no): ').lower()
            if answer == 'yes':
                # Reset the game board
                is_answer_valid = True
                GAME_RUNNING = True
                for i in range(3):
                    for j in range(3):
                        self.board[i][j] = ' '
                self.available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                # Ask the user if they want to change the level
                level_change = None
                while level_change not in ['yes', 'no']:
                    level_change = input('\n Do you want to change the '
                                         'difficulty? (yes/no): ').lower()
                    if level_change not in ['yes', 'no']:
                        print(f'\n{r}Invalid input. Enter "yes" or "no".\n{w}')
                    elif level_change == 'yes':
                        self.level_choice()

                print('\n ---------------')
                print(f'    {messages["new-game"]}')
                print(' ---------------')
            elif answer == 'no':
                is_answer_valid = True
                GAME_RUNNING = False
                print(f'\n {messages["thank you"]}\n')
            else:
                is_answer_valid = False
                print(f'\n{r} Invalid input Enter "yes" or "no"{w}\n')

    def level_choice(self):
        '''
        Get the difficulty level the player wants to play
        '''
        is_level_valid = False
        while is_level_valid is False:
            try:
                self.level = int(input('\n What level do you want to play?\n'
                                       ' 1. Easy\n 2. Medium\n '))
                if self.level not in [1, 2]:
                    is_level_valid = False
                    raise ValueError
                else:
                    is_level_valid = True
            except ValueError:
                print(f'\n{r} Invalid input. Enter from the options above.{w}')


GAME_RUNNING = True


def main():
    '''
    The function that runs the game
    '''
    # Start the game
    game = TicTacToe()

    # Print the welcome header
    print(messages['welcome'])
    print(messages['TTT'])
    print(messages['rules-info'])

    # Get the difficulty level
    game.level_choice()

    while (game.winner is None) and GAME_RUNNING:
        game.print_board()
        moves = game.available_moves()
        user_move = UserPlayer().get_valid_user_move(moves, game)
        game.append_move_to_board(user_move)
        game.check_for_win()
        game.check_for_tie()
        if game.winner is not None:
            game.winner = None
            continue
        game.change_player()
        # Change the randomness of the computer choice based on the user input
        if game.level == 1:
            cpu_move = ComputerPlayer().get_valid_computer_move(game)
        elif game.level == 2:
            cpu_move = ComputerPlayer().get_valid_medium_computer_move(game)

        # This is for when all squares are taken and X makes the last move
        try:
            game.append_move_to_board(cpu_move)
        except TypeError:
            print()
        game.check_for_win()
        game.check_for_tie()
        if game.winner is not None:
            game.winner = None
            game.change_player()
            continue
        game.change_player()


main()
