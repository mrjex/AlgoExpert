# command: "python sudoku-solver.py"

# Given the assumption that the board always is of size 9x9, the following conclusion is made about the algorithm's complexity:
# Time Complexity: O(1)
# Space Complexity: O(1)
def solveSudoku(board):
    solvePartialSudoku(0, 0, board)
    return board


def solvePartialSudoku(row, col, board):
    currentRow = row
    currentCol = col

    if currentCol == len(board[row]): # Increment row and reset column once prior row is traversed
        currentRow += 1
        currentCol = 0

        if (currentRow == len(board)): # Algorithm is done, return true
            return True

    if board[currentRow][currentCol] == 0: # If the current board-place is empty, then try to fill it with a digit
        return tryDigitsAtPosition(currentRow, currentCol, board)

    return solvePartialSudoku(currentRow, currentCol + 1, board) # Do nothing except increment the column if the current column already is valid


def tryDigitsAtPosition(row, col, board):
    for digit in range(1, 10): # Try digits from 0-9
        if isValidAtPosition(digit, row, col, board):
            board[row][col] = digit # Add it on the sudoku board temporarily to possibly backtrack it later

            if solvePartialSudoku(row, col + 1, board):
                return True

    # If we weren't able to solve the board with the current digit insertion attempt
    board[row][col] = 0
    return False

def isValidAtPosition(value, row, col, board):
    rowIsValid = value not in board[row]
    colIsValid = value not in map(lambda r: r[col], board)

    if not rowIsValid or not colIsValid:
        return False
    
    # Retrieve the starting position in the 9x9 board-grid, where each subgrid is of size 3x3
    subgridRowStart = row // 3
    subgridColStart = col // 3

    for rowIdx in range(3):
        for colIdx in range(3):
            # Transform indices to their equivalent position in the entire board
            rowToCheck = (subgridRowStart * 3) + rowIdx
            colToCheck = (subgridColStart * 3) + colIdx

            existingValue = board[rowToCheck][colToCheck]

            # If the value we are trying to add already exists in the subgrid, then return false
            if existingValue == value:
                return False
            
    return True # The current value is valid to place in the current position (row, col)



# Create boards, solve them and compare output to expected values
def runTests():

    # Create boards:

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    board2 = [
        [0, 0, 0, 0, 3, 0, 0, 0, 9],
        [0, 4, 0, 5, 0, 0, 0, 7, 8],
        [2, 9, 0, 0, 0, 1, 0, 5, 0],
        [0, 7, 8, 0, 0, 3, 0, 0, 6],
        [0, 3, 0, 0, 6, 0, 0, 8, 0],
        [6, 0, 0, 8, 0, 0, 9, 3, 0],
        [0, 6, 0, 9, 0, 0, 0, 2, 7],
        [7, 2, 0, 0, 0, 5, 0, 6, 0],
        [8, 0, 0, 0, 7, 0, 0, 0, 0]
    ]

    board3 = [
        [0, 2, 0, 0, 9, 0, 1, 0, 0],
        [0, 0, 7, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 6, 0],
        [0, 0, 1, 9, 0, 4, 0, 0, 0],
        [0, 0, 0, 6, 0, 5, 0, 0, 7],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 8, 5],
        [4, 9, 0, 0, 3, 0, 0, 0, 0]
    ]

    # Run tests
    print("SUDOKU TESTS:")

    print("")
    print("BOARD1:")
    print(solveSudoku(board))

    print("")
    print("BOARD2:")
    print(solveSudoku(board2))

    print("")
    print("BOARD2:")
    print(solveSudoku(board3))


runTests()