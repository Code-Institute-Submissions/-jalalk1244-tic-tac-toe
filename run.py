
board = [
        [' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']
        ]

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

print_board()