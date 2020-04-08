# kelvin du
# 101152192
import random


def placeMines():
    """
    placeMines() -> returns a 2d list that represents a game board filled with mines
    """
    # initialize a 2d matrix filled with 0s
    grid = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    # parse through the matrix and give values to cells
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            mineHere = random.randint(0, MINE_CHANCE)  # 1 in 10 chance for a mine
            if mineHere == 1:
                grid[row][col] = "X"
            else:
                grid[row][col] = ""
    return grid


def makeBoard():
    """
    makeBoard() -> returns a 2d list that represents a game board
    """
    grid = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            grid[row][col] = "#"
    return grid


def showBoard(board):
    """
    showBoard(board) -> passes in the gameboard and prints the board
    """
    numCol = " |"
    header = "--"
    for i in range(GRID_SIZE):
        numCol += str(i)
        header += "-"
    print(numCol)
    print(header)
    for row in range(GRID_SIZE):
        print(row, end = "")
        print("|",end = "")
        for col in range(GRID_SIZE):
            if board[row][col] == "":
                print(" ", end = "")
            print(board[row][col], end = "")
        print("")


def countHiddenCells(board):
    """
    countHiddenCells(board) -> passes in gameboard and returns number of unrevealed cells
    """
    unrevealed = 0
    # parse through game board
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "#":
                unrevealed += 1  # add to unrevealed count
    return unrevealed


def countAllMines(board):
    """
    countAllMines(board) -> passes a gameboard that contains mines and returns the number of mines
    """
    mineCount = 0
    # parse through the board to count mines
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "X":
                mineCount += 1
    return mineCount


def isMineAt(board, row, col):
    """
    isMineAt(board, row, col) -> passes in a game board, x,y coordinates and returns a boolean if
    a mine is at the coordinate
    """
    if board[row][col] == "X":
        return True
    else:
        return False


def countAdjacentMines(board, x, y):
    """
    countAdjacentMines(board, x, y) -> passes in a game board and retuns the adjacent number of cells
    """
    adjacentMines = 0
    for newX in range(x - 1, x + 2):
        if 0 <= newX < GRID_SIZE:
            for newY in range(y - 1, y + 2):
                # print(newX, newY)
                if 0 <= newY < GRID_SIZE and board[newY][newX] == "X":
                    # print("mines")
                    adjacentMines += 1
    return adjacentMines


def reveal(gameBoard, mineBoard, x, y):
    """
    reveal(gameBoard, mineBoard, x, y) -> passes in a player board and game board, and xy coordinates
    reveals empty cells or reveals all bombs when player loses
    """
    # if there is an empty cell continue to reveal adjacent empty cells
    if mineBoard[y][x] == "":
        mines = countAdjacentMines(mineBoard, x, y)
        if mines != 0:
            # show cell with adjacent mines
            gameBoard[y][x] = mines
        else:
            # make cell a space to keep the scale
            gameBoard[y][x] = " "
            # reveals the next cell
            for newX in range(x-1, x+2):
                if 0 <= newX < GRID_SIZE:
                    for newY in range(y - 1, y + 2):
                        # print(newX, newY)
                        if 0 <= newY < GRID_SIZE and gameBoard[newY][newX] == "#":
                            reveal(gameBoard, mineBoard, newX, newY)
        # gameBoard[x][y] = " "
        # if mines == 0:
        # else:
        #     gameBoard[x][y] = mines
    else:  # if player loses run this block
    # reveals all mines in the board
        for row in range(len(mineBoard)):
            for col in range(len(mineBoard)):
                if mineBoard[row][col] == "X":
                    gameBoard[row][col] = "X"

def inputValid(text):
    """
    inputValid(text) -> passes in a string and does various tests to check for
    input validity, returns a boolean if passes/fails test
    """
    # check if has comma
    if "," not in text:
        return False
        # if it does split by comma
    temp = text.split(",")
    if len(temp) != 2:
        return False

    # check if there are only 2 values and both are numbers
    if not (temp[0].isdigit() and temp[1].isdigit()):
        return False
    if not (0 <= int(temp[0]) <= GRID_SIZE and 0 <= int(temp[1]) <= GRID_SIZE):
        return False
    return True

def main():
    gameLoop = True
    # initialize boards
    mineBoard = placeMines()
    playerBoard = makeBoard()
    # prints the starting board
    showBoard(playerBoard)
    while gameLoop:
        coord = input("Select a cell '(row,col)' > ")
        if inputValid(coord):
            coordList = coord.split(",")
            # print(countAdjacentMines(mineBoard, int(coordList[1]),  int(coordList[0])))
            # check if there is a mine at the coordinate
            if isMineAt(mineBoard, int(coordList[0]), int(coordList[1])):
                # if there is a mine then reveal the board because game over
                reveal(playerBoard, mineBoard, int(coordList[1]), int(coordList[0]))
                # display the board with all mines
                showBoard(playerBoard)
                gameLoop = False
                print("GAME OVER!")
            else:
                # check to reveal the rest of the empty cells
                reveal(playerBoard, mineBoard, int(coordList[1]), int(coordList[0]))
                showBoard(playerBoard)
                # if board is complete then player wins game
                if countHiddenCells(playerBoard) - countAllMines(mineBoard) <= 0:
                    gameLoop = False
                    print("You WIN!")

GRID_SIZE = 5
MINE_CHANCE = 10
main()
