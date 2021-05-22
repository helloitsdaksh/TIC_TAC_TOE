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

def rowcrossed(grid):

    for i in range(3):
        if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][0] != ' ':
            return (True)
    return False

def columncrossed(grid):

    for i in range(3):
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i] != ' ':
            return (True)
    return False

def diagonalcrossed(grid):

    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return (True)

    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != ' ':      
        return (True)
  
    return(False)