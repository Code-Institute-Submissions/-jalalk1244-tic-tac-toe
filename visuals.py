'''
The module with the cisuals and game messages
'''

'''
The COLORS dictionary and color_text function was taken from:
github name: richardbwest
Date: 2022-09-25
Title of program/source code: demo1.py
Web address: https://gist.github.com/richardbwest/17674f84961e975d47cf106da9728dd2'''   

COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "light-yellow": "\u001b[33m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[0m",
    "cyan-background": "\u001b[46;1m",
    'green-background': '\u001b[42m',
    "bold": "\u001b[1m"
}


def color_text(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


# Representing colors with thier firsrt letter
r = COLORS["red"]
m = COLORS["magenta"]
c = COLORS["cyan"]
y = COLORS["yellow"]
ly = COLORS["light-yellow"]
w = COLORS["white"]
b = COLORS['blue']
gb = COLORS['green-background']
bb = COLORS['black-background']
cb = COLORS['cyan-background']
yb = COLORS['yellow-background']
bold = COLORS["bold"]

welcome_message = f'''{c}
 __          __  _                               _        {y}
 \ \        / / | |                             | |       {m}
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | |_ ___  {c}
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | __/ _ \ {y}
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | || (_) |{m}
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|     \__\___/ {c}
  {w}                                                     
'''
tic_tac_toe = f'''{c}
  _______ _       {y} _______          {m} _______         {c}
 |__   __(_)      {y}|__   __|         {m}|__   __|        {c}
    | |   _  ___  {y}   | | __ _  ___  {m}   | | ___   ___ {c}
    | |  | |/ __| {y}   | |/ _` |/ __| {m}   | |/ _ \ / _ \ {c}
    | |  | | (__  {y}   | | (_| | (__  {m}   | | (_) |  __/{c}
    |_|  |_|\___| {y}   |_|\__,_|\___| {m}   |_|\___/ \___|{c}                                              
 {w}                                                    
'''

# The bord colors
board_line = f'\n{b}+{m}---{b}+{m}---{b}+{m}---{b}+{w}'
board_side = f'{m}|{w}'

# The player letter colors
x_player = f'{c}X{w}'
o_player = f'{ly}O{w}'

# The invalid input messages
too_small_big_number = f'\n{r} You can only pick squares between 1-9. Please try again!{w}\n' 
taken_square = f'\n{r} The square is already taken. Please choose another one!{w}\n'
invalid_input = f'\n{r} Invalid input, please try again!{w}\n'

rules = f'''
{bold} How to play{w}
 1. You choose a square between 1-9 from the available ones.
 2. You are {c}X{w}, the computer  is {ly}O{w}. Players take turns putting their marks in empty squares.
 3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
 4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
'''

new_game = f'{y}Ne{m}w Ga{c}me{w}'

messages = {
  'welcome': welcome_message,
  'TTT': tic_tac_toe,
  "board-line": board_line,
  'side-line': board_side,
  'x-letter': x_player,
  'o-letter': o_player,
  'not-in-range': too_small_big_number,
  'square-taken': taken_square,
  'not-alpha': invalid_input,
  'rules-info': rules,
  'new-game': new_game,
}