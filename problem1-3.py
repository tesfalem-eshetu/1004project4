import numpy as np
from matplotlib import pyplot as plt
import maze

PATH = 0  # The cell contains a passageway
WALL = 1  # The cell contains a wall
THESEUS = 2  # Theseus is in this cell
THREAD = 3  # The cell contains Ariadne's thread
MINOTAUR = 4  # The Minotaur is in this cell
VISITED = 5  # Special marker for the cells visited by Theseus


def build_labyrinth(width, height, plan):

    labyrinth = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            if plan[i * width + j]:
                labyrinth[i][j] = WALL

    labyrinth[0][1] = THESEUS
    labyrinth[-2][-2] = MINOTAUR

    return labyrinth

def slay(labyrinth, y, x):

    if labyrinth[y][x] == WALL or labyrinth[y][x] == VISITED:
        return False
    elif labyrinth[y][x] == MINOTAUR:
        return True
    else:
        labyrinth[y][x] = VISITED
        # this one will be checking every direction
        if slay(labyrinth, y, x+1) == True or slay(labyrinth, y, x-1) == True or slay(labyrinth, y+1,x) == True or slay(labyrinth, y-1, x) == True:
            labyrinth[y][x] = THREAD
            return True
        else:
            return False


if __name__ == '__main__':
    # this one will be generating a new maze everytime the main is callled
    width, height, plan = maze.generate()

    #  this one will help us to Convert the maze to a labyrinth
    labyrinth = build_labyrinth(width, height, plan)

    # Navigate Theseus to slay the Minotaur
    slay(labyrinth, 0, 1)

    # Show the result
    plt.imshow(labyrinth)
    plt.show()
