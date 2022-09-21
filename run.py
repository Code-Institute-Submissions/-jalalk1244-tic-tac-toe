
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

WINNER = None
current_player = 'X'


def print_board():
    '''
    Print the tic tac toe game board
    '''

    rows = 3
    columns = 3

    for row in range(rows):
        print('\n+---+---+---+')
        print('|', end='')
        for column in range(columns):
            print('', board[row][column], end=' |')
    print('\n+---+---+---+')


def available_moves():
    '''
    Returns all the available squares that the player can make a move on
    '''
    moves = []

    for row in range(3):
        for column in range(3):
            moves.append(board[row][column])
    return moves


def get_valid_user_move(moves):
    '''
    Let the user pick a square
    Check if the square is in the board
    '''
    is_square_valid = False
    player_move = None

    while not is_square_valid:
        picked_square = input('Pick a square between 1-9: ')

        try:
            player_move = int(picked_square)
            if player_move not in range(1, 10) or moves[player_move - 1] != ' ':
                raise ValueError
            else:
                is_square_valid = True
        except ValueError:
            print('Invalid sqaure, please try again!')
    return player_move


def append_move_to_board(move):
    '''
    Add the player move to the board if it is a valid move
    Remove the square from the avaible moves
    '''

    if move >= 1 and move <= 3:
        board[0][move-1] = current_player
    elif move >= 4 and move <= 6:
        board[1][move-4] = current_player
    elif move >= 7 and move <= 9:
        board[2][move-7] = current_player
    del available_moves()[move - 1]


while ' ' in board[0] or ' ' in board[1] or ' ' in board[2]:
    print_board()
    t = available_moves()
    h = get_valid_user_move(t)
    append_move_to_board(h)
