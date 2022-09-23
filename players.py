import random


class ComputerPlayer:
    '''
    A class to represent the computer player
    '''
    def get_valid_computer_move(game):
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

    def get_valid_user_move(moves, game):
        '''
        Let the user pick a square
        Check if the square is in the game board
        '''
        is_square_valid = False
        player_move = None
        turn = ['X' if current_letter == 'O' else 'O']

    while not is_square_valid:
        picked_square = input('Pick a square between 1-9: ')

        try:
            player_move = int(picked_square)
            if player_move not in range(1, 10):
                print('You can only pick squares between 1-9. Please try again!')
            elif moves[player_move - 1] != ' ':
                print('The square is already taken, choose another one.')
            else:
                moves.insert(player_move - 1, 'X')
                game.available_squares.remove(player_move)
                # print(f'\n{current_letter} has moved to square {player_move}')
                # print(f'\nIt is {turn[0]}:s turn')
                is_square_valid = True
        except ValueError:
            print('Invalid input, please try again!')
    return player_move
