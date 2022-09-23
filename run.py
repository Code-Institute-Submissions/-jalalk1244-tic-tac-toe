import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

WINNER = None
current_letter = 'X'
available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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
            if player_move not in range(1, 10):
                print('You can only pick squares between 1-9. Please try again!')
            elif moves[player_move - 1] != ' ':
                print('The square is already taken, choose another one.')
            else:
                moves.insert(player_move - 1, 'X')
                available_squares.remove(player_move)
                # print(f'\n{current_letter} has moved to square {player_move}')
                # print(f'\nIt is {turn[0]}:s turn')
                is_square_valid = True
        except ValueError:
            print('Invalid input, please try again!')
    return player_move


def append_move_to_board(move):
    '''
    Add the player move to the board if it is a valid move
    Remove the square from the avaible moves
    '''
    turn = ['X' if current_letter == 'O' else 'O']

    if move >= 1 and move <= 3:
        board[0][move-1] = current_letter
    elif move >= 4 and move <= 6:
        board[1][move-4] = current_letter
    elif move >= 7 and move <= 9:
        board[2][move-7] = current_letter
    del available_moves()[move - 1]

    print(f'{current_letter} has moved to square {move}\n')
    print(f"It is {turn[0]}'s turn")


def check_for_win():
    '''
    Check if the player has won:
     - horizontally
     - vertically
     - Diagonally
    '''
    global game_running, current_letter
    vertical_win_row = [[], [], []]
    diagonal_win = [[], [], []]
    j = 2

    for i in range(3):
        diagonal_win[0].append(board[i][i])
        diagonal_win[1].append(board[j][i])
        j = j - 1
        for j in range(3):
            vertical_win_row[i].append(board[j][i])

    for i in range(3):
        # Check for horizontal win 
        if board[i].count(current_letter) == 3:
            winner = current_letter
            print(f'\n{winner} has won!')
            game_running = False
            print_board()
            break
        # Check for vertical win
        elif vertical_win_row[i].count(current_letter) == 3:
            winner = current_letter
            print_board()
            print(f'\n{winner} has won!')
            game_running = False
            break
        # Check for diagonal win
        elif diagonal_win[i].count(current_letter) == 3:
            winner = current_letter
            print_board()
            print(f'\n{winner} has won!')
            game_running = False
            break


def change_player():
    '''
    switch players
    '''
    global current_letter
    if current_letter == 'X':
        current_letter = 'O'
    else:
        current_letter = 'X'


def computer_move():
    '''
    Returns a random computer move from the available squares 
    '''
    try:
        pc = random.choice(available_squares)
        available_squares.remove(pc)
        return pc
    except IndexError:
        print()


game_running = True
while (' ' in board[0] or ' ' in board[1] or ' ' in board[2]) and game_running:
    print_board()
    moves = available_moves()
    user_move = get_valid_user_move(moves)
    append_move_to_board(user_move)
    check_for_win()
    change_player()
    print(moves)
    cpu_move = computer_move()
    try:
        append_move_to_board(cpu_move)
    except TypeError:
        print()
    check_for_win()
    change_player()
