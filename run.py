import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

WINNER = None
current_letter = 'X'


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
    turn = ['X' if current_letter == 'O' else 'O']

    while not is_square_valid:
        picked_square = input('Pick a square between 1-9: ')

        try:
            player_move = int(picked_square)
            if player_move not in range(1, 10) or moves[player_move - 1] != ' ':
                raise ValueError
            else:
                is_square_valid = True
                print(f'\n{current_letter} has moved to square {player_move}')
                print(f'\nIt is {turn[0]}:s turn')
        except ValueError:
            print('Invalid sqaure, please try again!')
    return player_move


def append_move_to_board(move):
    '''
    Add the player move to the board if it is a valid move
    Remove the square from the avaible moves
    '''

    if move >= 1 and move <= 3:
        board[0][move-1] = current_letter
    elif move >= 4 and move <= 6:
        board[1][move-4] = current_letter
    elif move >= 7 and move <= 9:
        board[2][move-7] = current_letter
    del available_moves()[move - 1]


def check_for_win():
    '''
    Check if the player has won either:
     - horizontally
     - vertically
     - Diagonally
    '''
    global game_running

    # Check for horizontal win
    for i in range(3):
        if board[i].count(current_letter) == 3:
            winner = current_letter
            print_board()
            print(f'\n{winner} has won!')
            game_running = False
            break
    # Check for vertical win
    vertical_win_row = [[], [], []]
    for i in range(3):
        for j in range(3):
            vertical_win_row[i].append(board[j][i])

    for i in range(3):
        if vertical_win_row[i].count(current_letter) == 3:
            winner = current_letter
            print_board()
            print(f'\n{winner} has won!')
            game_running = False
            break
    # Check for diagonal win
    diagonal_win_1 = []
    diagonal_win_2 = []

    j = 2
    for i in range(3):
        diagonal_win_1.append(board[i][i])
        diagonal_win_2.append(board[j][i])
        j -= 1

    if diagonal_win_1.count(current_letter) == 3 or diagonal_win_2.count(current_letter) == 3:
        winner = current_letter
        print_board()
        print(f'\n{winner} has won!')
        game_running = False


def change_player():
    '''
    switch players
    '''
    global current_letter
    if current_letter == 'X':
        current_letter = 'O'
    else:
        current_letter = 'X'


def computer_move(moves):
    '''
    Returns a random computer move from the available squares 
    '''
    valid_move = False
    while valid_move is False:
        random_computer_move = random.randint(1, 9)
        if moves[random_computer_move - 1] != ' ':
            valid_move = False
        else:
            moves.insert(random_computer_move - 1, 'O')
            valid_move = True
    return random_computer_move


game_running = True
while (' ' in board[0] or ' ' in board[1] or ' ' in board[2]) and game_running:
    print_board()
    moves = available_moves()
    user_move = get_valid_user_move(moves)
    append_move_to_board(user_move)
    check_for_win()
    change_player()
    print(moves)
    cpu_move = computer_move(moves)
    append_move_to_board(cpu_move)
    check_for_win()
    change_player()
