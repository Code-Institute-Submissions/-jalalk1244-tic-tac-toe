'''
The module with the cisuals and game messages
'''
import os

'''
The COLORS dictionary and color_text function was taken from:
github name: richardbwest
Date: 2022-09-25
Title of program/source code: demo1.py
Web address: https://gist.github.com/richardbwest/17674f84961e975d47cf106da9728dd2'''

os.system("cls")  # use this for windows. change to os.system("clear") for linux

COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


def color_text(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
