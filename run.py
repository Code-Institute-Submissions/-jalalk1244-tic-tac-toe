
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

WINNER = None


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


def get_valid_user_move():
    '''
    Let the user pick a square
    Check if the square is in the board
    '''
    num_range = [1, 2, 3, 4, 5, 6, 8, 9]
    is_square_valid = False

    while not is_square_valid:
        picked_square = int(input('Pick a square between 1-9: '))

        if picked_square not in num_range:
            print('Invalid input, Please pick a valid square!')
            is_square_valid = False
        else:
            print('Valid number')
            is_square_valid = True


t = available_moves()

print(t)
