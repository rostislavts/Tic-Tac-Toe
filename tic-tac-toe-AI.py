# Simple Tic-Tac-Toe game 
# Procedure code

import random

def print_grid(grid):
    print("---------")
    for i in range(3):
        row = "| "
        for j in range(3):
            row += grid[i][j] + " " 
        row += "|"
        print(row)
    print("---------")

def has_three_in_a_row(letter, grid): # X or O
    return has_three_horizontally(letter, grid) or has_three_vertically(letter, grid) or has_three_diagonally(letter, grid) 

def has_three_horizontally(letter, grid):
    for i in range(3):
        counter = 0
        for j in range(3):
            if grid[i][j] == letter:
                counter += 1
        if counter == 3:
            return True
    return False        

def has_three_vertically(letter, grid):
    for j in range(3):
        counter = 0
        for i in range(3):
            if grid[i][j] == letter:
                counter += 1
        if counter == 3:
            return True
    return False

def has_three_diagonally(letter, grid):
    main_diag_cnt = 0
    snd_diag_cnt = 0
    for i in range(3):
        for j in range(3):
            if i == j and grid[i][j] == letter: # main diagonal
                main_diag_cnt += 1
            if i == len(grid) - j - 1 and grid[i][j] == letter: # secondary diagonal
                snd_diag_cnt += 1     
    return main_diag_cnt == 3 or snd_diag_cnt == 3

def has_empty_cell(grid):
    for row in grid:
        if "_" in row or " " in row:
            return True
    return False

def is_valid_format(coordinates):
    return len(coordinates) == 3 and coordinates[0].isdigit() and coordinates[1] == ' ' and coordinates[2].isdigit()  

def is_valid_coordinates(coordinates):
    if not is_valid_format(coordinates):
        return False
    fst_coord = int(coordinates[0])
    snd_coord = int(coordinates[2])
    return 0 <= fst_coord and fst_coord <= 3 and 0 <= snd_coord and snd_coord <= 3

def is_occupied(i, j, grid):
    return  i == -1 and j == -1 or grid[i][j] != ' ' and grid[i][j] != '_'

def read_coordinates(grid, is_player_x_turn):
    coordinates = ""
    i = -1
    j = -1

    while not is_valid_coordinates(coordinates) or is_occupied(i, j, grid):
        if is_player_x_turn:
            coordinates = input("Enter the coordinates: > ")
        else:
            coordinates = str(random.randint(1,3)) + " " + str(random.randint(1,3))

        if not is_valid_format(coordinates):
            print("You should enter numbers!")
        elif not is_valid_coordinates(coordinates):
            print("Coordinates should be from 1 to 3!") 
        else:
            fst_coord = int(coordinates[0])
            snd_coord = int(coordinates[2])

            # Index formula : (x, y) --> (3-y, x-1)
            i = 3 - snd_coord
            j = fst_coord - 1 

            if is_occupied(i, j, grid):
                print("This cell is occupied! Choose another one!")
    return (i, j)   

def print_info():
    print("""\t\tPOSITIONS 
            (1,3) (2,3) (3,3)
            (1,2) (2,2) (3,2)
            (1,1) (2,1) (3,1)
          """)

def main():
    #print_info()

    cells = "         "
    grid = [ list(cells[i:i+3]) for i in range(0,9,3) ]

    is_gameover = False
    is_player_x_turn = True

    print_grid(grid)
    while not is_gameover:
        coords = read_coordinates(grid, is_player_x_turn)
        i = coords[0]
        j = coords[1]
        
        if is_player_x_turn:
            grid[i][j] = 'X'
        else:
            grid[i][j] = 'O' 

        is_player_x_turn = not is_player_x_turn

        print_grid(grid)
        print('Making move level "easy"')

        x_wins = has_three_in_a_row("X", grid)
        o_wins = has_three_in_a_row("O", grid)
        is_end_without_a_winner = not x_wins and not o_wins and not has_empty_cell(grid)
        is_gameover = is_end_without_a_winner or x_wins or o_wins

    if is_end_without_a_winner:
        print("Draw")
    elif x_wins:
        print("X wins")    
    elif o_wins:
        print("O wins")

main()