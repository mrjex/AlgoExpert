def spiralTraverse(array):
    outArr = []
    startRow, endRow = 0, len(array) - 1
    startColumn, endColumn = 0, len(array[0]) - 1


    while startRow <= endRow and startColumn <= endColumn:
        # Right
        for i in range(startColumn, endColumn + 1):
            outArr.append(array[startRow][i])

        # Down
        for i in range(startRow + 1, endRow + 1):
            outArr.append(array[i][endColumn])

        # Left
        for i in reversed(range(startColumn, endColumn)):
            if startRow == endRow:
                break
            outArr.append(array[endRow][i])

        # Up
        for i in reversed(range(startRow + 1, endRow)):
            if startColumn == endColumn:
                break
            outArr.append(array[i][startColumn])

        startRow += 1
        endRow -= 1
        startColumn += 1
        endColumn -= 1

    return outArr

def runTestCases():
    print("")
    print("")
    print("spiral-traverse.py:")

    print(spiralTraverse([
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ])) # Expected output: Ascending order

    print(spiralTraverse([
        [1, 2, 3],
        [12, 13, 4],
        [11, 14, 5],
        [10, 15, 6],
        [9, 8, 7]
    ])) # Expected output: Ascending order

runTestCases()