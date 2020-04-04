#kelvin du
#101152192
import random
'''

'''
def placeMines():
    grid = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            mineHere = random.randint(0, MINE_CHANCE)
            if mineHere == 1:
                grid[row][col] = "X"
            else:
                grid[row][col] = ""
    return grid

def makeBoard():
    grid = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            grid[row][col] = "#"
    return grid

def showBoard(board):
    numRow = ""
    header = ""
    for i in range(GRID_SIZE):
        numRow += str(i)
        header += "-"
    print(numRow)
    print(header)

def countHiddenCells(board):
    unrevealed = 0
    for row in board:
        for tile in board:
            if tile == "#":
                unrevealed += 1
    return unrevealed

def countAllMines(board):
    mineCount = 0
    for row in board:
        for tile in board:
            if tile == "X":
                mineCount += 1
    return mineCount

def isMineAt(board, x, y):
    print()

def countAdjacentMines(matrix):
    print()

def main():
    print(placeMines())
    print(showBoard(makeBoard()))

GRID_SIZE = 5
MINE_CHANCE = 10
main()
