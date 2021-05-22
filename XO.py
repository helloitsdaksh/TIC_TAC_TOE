import numpy as np

grid = [["1","2","3"], 
        ["4","5","6"],
        ["7","8","9"]]

player_one = ""
player_two = ""

def choice():
    player_one = input("Enter Your Choice Player one, 'X' or 'O':")
    if player_one.upper() == "X":
        player_two = "O"
    elif player_one.upper() == "O":
        player_two = "X"
    return player_one,player_two