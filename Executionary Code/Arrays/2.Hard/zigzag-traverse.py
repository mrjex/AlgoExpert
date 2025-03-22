# O(n) time | O(n) space
def zigzagTraverse(array):
    amountOfRows = len(array)
    amountOfColumns = len(array[0])

    currentDirection = "Down"
    outArr = []

    i = 0
    j = 0

    while len(outArr) < (amountOfRows * amountOfColumns):
        outArr.append(array[i][j])
        if currentDirection == "Down":
            if j == 0 or i == amountOfRows - 1:
                if i == amountOfRows - 1:
                    j += 1
                else:
                    i += 1
                currentDirection = "Up"
            else:
                i += 1
                j -= 1

        elif currentDirection == "Up":
            if i == 0 or j == amountOfColumns - 1:
                if j == amountOfColumns - 1:
                    i += 1
                else:
                    j += 1
                currentDirection = "Down"
            else:
                i -= 1
                j += 1

    return outArr

def runTestCases():
    print("")
    print("")
    print("zigzag-traverse.py:")

    print(zigzagTraverse(
    [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ]
    )) # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    print(zigzagTraverse(
    [
        [1, 3, 4, 10, 11, 20],
        [2, 5, 9, 12, 19, 21],
        [6, 8, 13, 18, 22, 27],
        [7, 14, 17, 23, 26, 28],
        [15, 16, 24, 25, 29, 30]
    ]
    )) # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


runTestCases()