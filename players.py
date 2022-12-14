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
            pc_choice = random.choice(game.available_squares)
            game.available_squares.remove(pc_choice)
            return pc_choice
        except IndexError:
            print()

    def get_valid_medium_computer_move(self, game):
        '''
        Reduces the randomness of the computer choice
        '''

        flat_board = sum(game.board, [])

        # All the possible winning combinations in tic tac toe
        possible_ways_to_win = [[1, 2, 3],
                                [1, 4, 7],
                                [1, 5, 9],
                                [2, 5, 8],
                                [3, 6, 9],
                                [3, 5, 7],
                                [4, 5, 6],
                                [7, 8, 9]]

        # If in any of the winnig combinations,
        # 2 of them is taken choose the third one
        # i.e  if one and 3 is x/o choose return 2
        for way in possible_ways_to_win:
            if (
                    (flat_board[way[0] - 1] == flat_board[way[1] - 1])
                    and flat_board[way[0] - 1] != ' '
               ):
                if way[2] in game.available_squares:
                    game.available_squares.remove(way[2])
                    pc_choice = way[2]
                    return pc_choice
            elif (
                    (flat_board[way[0] - 1] == flat_board[way[2] - 1])
                    and flat_board[way[0] - 1] != ' '
                 ):
                if way[1] in game.available_squares:
                    game.available_squares.remove(way[1])
                    pc_choice = way[1]
                    return pc_choice
            elif (
                    (flat_board[way[1] - 1] == flat_board[way[2] - 1])
                    and flat_board[way[1] - 1] != ' '
                 ):
                if way[0] in game.available_squares:
                    game.available_squares.remove(way[0])
                    pc_choice = way[0]
                    return pc_choice
            elif (
                    flat_board[8] == ' ' or flat_board[0] == ' '
                    or flat_board[6] == ' ' or flat_board[2] == ' '
                 ):

                if flat_board[8] == ' ':
                    pc_choice = 9
                elif flat_board[6] == ' ':
                    pc_choice = 7
                elif flat_board[2] == ' ':
                    pc_choice = 3
                else:
                    pc_choice = 1
                game.available_squares.remove(pc_choice)
                return pc_choice
            else:
                pc_choice = random.choice(game.available_squares)
                game.available_squares.remove(pc_choice)
                return pc_choice


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
                    is_square_valid = True
            except ValueError:
                print(messages['not-alpha'])
        return player_move
