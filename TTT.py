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

def gameOver(grid):
    
    return (rowcrossed(grid) or columncrossed(grid) or diagonalcrossed(grid))


def entry(one,two,count):
    # position = {'1':'grid[0][0]','2':grid[0][1], '3':grid[0][2], '4':grid[1][0], '5':grid[1][1],'6':grid[1][2],'7':grid[2][0],'8':grid[2][1],'9':grid[2][2]}
    if gameOver(grid) == False and count == 9:
        print("It's a draw")

    elif gameOver(grid) == True:
        if count % 2 == 1 :
            print("Player 1 is Winner!!")
        
        else:
            print("Player 2 is Winner!!")

    while (gameOver(grid) == False and count != 9):
        if count % 2 == 0: 
            play_one = input(f"Its player 1 chance, where would you like to enter {one} :")
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == play_one:
                        grid[i][j] = one
                        count += 1
                        print(np.matrix(grid))
                        entry(one,two,count)


        else :
            play_two = input(f"Its player 2 chance, where would you like to enter {two} :")
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == play_two:
                        grid[i][j] = two
                        count += 1
                        print(np.matrix(grid))
                        entry(one,two,count)
    



if __name__ == "__main__":
    count = 0
    x,y = choice()
    print({'Player One' : x,'Player Two' : y})
    entry(x,y,count)
    print(np.matrix(grid))