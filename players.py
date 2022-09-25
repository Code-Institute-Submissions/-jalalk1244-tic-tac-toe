'''
The module with the player classes
'''

import random
from visuals import messages


class ComputerPlayer:
    '''
    A class to represent the computer player
    '''
    def get_valid_computer_move(self, game):
        '''
        Returns a random computer move from the available squares
        '''
        try:
            pc = random.choice(game.available_squares)
            game.available_squares.remove(pc)
            return pc
        except IndexError:
            print()


class UserPlayer:
    '''
    A class for the user player
    '''

    def get_valid_user_move(self, moves, game):
        '''
        Let the user pick a square
        Check if the square is in the game board
        '''
        is_square_valid = False
        player_move = None
        # turn = ['X' if current_letter == 'O' else 'O']

        while not is_square_valid:
            picked_square = input('Pick a square between 1-9: ')

            try:
                player_move = int(picked_square)
                if player_move not in range(1, 10):
                    print(messages['not-in-range'])
                elif moves[player_move - 1] != ' ':
                    print(messages['square-taken'])
                else:
                    moves.insert(player_move - 1, 'X')
                    game.available_squares.remove(player_move)
                    # print(f'\n{current_letter} has moved to square {player_move}')
                    # print(f'\nIt is {turn[0]}:s turn')
                    is_square_valid = True
            except ValueError:
                print(messages['not-alpha'])
        return player_move
