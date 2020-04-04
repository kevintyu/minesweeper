# kelvin du
# 101152192
import random


def placeMines():
    """
    placeMines() -> returns a 2d list that represents a game board
    """
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
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "#":
                unrevealed += 1
    return unrevealed


def countAllMines(board):
    mineCount = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "X":
                mineCount += 1
    return mineCount


def isMineAt(board, row, col):
    if board[row][col] == "X":
        return True
    else:
        return False


def countAdjacentMines(board, row, col):
    print()


def reveal(board):

    return reveal()


def main():
    print(placeMines())
    print(showBoard(makeBoard()))
    print(countHiddenCells(makeBoard()))
    print(countAllMines(placeMines()))

GRID_SIZE = 5
MINE_CHANCE = 10
main()
