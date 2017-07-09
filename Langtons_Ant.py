# Jan 27, 2017 - Sam Abarbanel
# This script models "Langtons Ant." Search it up for a better understanding
from time import sleep


# Setting up directions for the ant
UP = [-1, 0]
RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]

directions = [UP, RIGHT, DOWN, LEFT] # This makes changing directions easier
direction_Pointer = 3 # Left

grid = [[0]] # 2D array that expands as ant crawls over it

ant_Position = [0, 0] # Where the ant is on the grid
ant_Direction = directions[direction_Pointer] # Left


def add_Boundary():
    if ant_Position[0] == 0 and ant_Direction == UP: # If the ant is going to step out of range in the up direction, 
        grid.insert(0, [' '] * len(grid[0])) # Append a blank row to where the ant is going to step

    if ant_Position[0] == (len(grid) - 1) and ant_Direction == DOWN: # If the ant is going to step out of range in the down direction,
        grid.append([' '] * len(grid[0])) # Add a row below where it is going to step

    if ant_Position[1] == 0 and ant_Direction == LEFT: # If the ant is going to step out of range in the left direction,
        for i in range(len(grid)):
            grid[i].insert(0, ' ') # Add a row where the ant is going to step
    
    if ant_Position[1] == (len(grid[0]) - 1) and ant_Direction == RIGHT: # If the ant is going to step out of range in the right direction,
        for i in range(len(grid)):
            grid[i].append(' ') # Add a row where the ant is going to step


for i in range(11000): # Number of steps the ant takes. 
    if grid[ant_Position[0]][ant_Position[1]] == 0 or grid[ant_Position[0]][ant_Position[1]] == ' ': # If ant lands on 0 or empty tile,
        left_Or_Right = 1 # Right
        bit = 1 # Flip bit to 1 if original bit is 0 or ' '
    else:
        left_Or_Right = -1 # Left
        bit = 0 # Flip bit to 0 if original bit is 1

    grid[ant_Position[0]][ant_Position[1]] = bit # Change bit
    direction_Pointer = (direction_Pointer + left_Or_Right) % 4 # Turn left or right
    ant_Direction = directions[direction_Pointer] # Redefine ant direction
    add_Boundary() # If the ant is going to step out of the grid, expand the grid to make room
        
    ant_Position[0] += ant_Direction[0] # Ant takes a step
    ant_Position[1] += ant_Direction[1]

    if ant_Position[1] == -1: # If ant causes the grid to expand in the negative direction,
        ant_Position[1] = 0 # then change the ant's coordinates so as not to cause an out-of-range error. 

    if ant_Position[0] == -1: # See two comments above
        ant_Position[0] = 0

    # This prints the grid like a square
    for i in range(len(grid)): # Each row
        for j in range(len(grid[0])): # Elements in each row
            print grid[i][j], # Prints each element of a whole row on one line
        print # Prints the finished line of elements
    sleep(0.1) # Buffer so you can see the ant step
    print "\n" * 50 # Refresh "frame"
