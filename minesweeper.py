#kelvin du
#101152192
'''

'''
def placeMines():
    grid = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            grid[row][col] = ""
    return grid

def makeBoard():
    grid = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            grid[row][col] = "#"
    return grid

def showBoard(board):
    print()

def countHiddenCells(matrix):
    print()

def countAllMines(matrix):
    print()

def isMineAt(matrix):
    print()

def countAdjacentMines(matrix):
    print()

def main():
    print(placeMines())
GRID_SIZE = 5
MINE_CHANCE = 10
main()
