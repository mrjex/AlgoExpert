# O(r * c * c) = O(r * c^2) time | O(3c) = O(c)
# Where r and c are the amount of rows and columns in the input array
def waterfallStreams(array, source):
    rows = len(array)
    columns = len(array[0])

    array[0][source] = -1
    waterState = array[0]

    for i in range(rows - 1):
        currentRow = waterState.copy()
        nextRow = array[i + 1]

        for j in range(columns):
            if nextRow[j] == 1:
                waterState[j] = 1
            elif nextRow[j] == 0 and waterState[j] == 1:
                waterState[j] = 0

            if currentRow[j] < 0:
                currentWaterValue = currentRow[j]

                if nextRow[j] == 0:
                    waterState[j] = min(waterState[j], currentWaterValue)

                elif nextRow[j] == 1:
                    leftIdx, rightIdx = j - 1, j + 1
                    newWaterValue = currentRow[j] / 2

                    while leftIdx >= 0:
                        if currentRow[leftIdx] <= 0 and nextRow[leftIdx] <= 0:
                            waterState[leftIdx] += newWaterValue
                            break

                        if currentRow[leftIdx] == 1:
                            break

                        leftIdx -= 1

                    while rightIdx < columns:
                        if currentRow[rightIdx] <= 0 and nextRow[rightIdx] <= 0:
                            waterState[rightIdx] += newWaterValue
                            break

                        if currentRow[rightIdx] == 1:
                            break

                        rightIdx += 1

    return list(map(lambda a: a * -100, waterState))


def runTestCases():
    print("")
    print("")
    print("waterfall-streams.py:")

    print(waterfallStreams(
    [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
    ], 3)) # Expected output: [0, 0, 0, 25, 25, 0, 0]

    print(waterfallStreams(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ], 8)) # Expected output: [25, 0, 12.5, 0, 4.6875, 0, 0, 0, 0, 7.8125, 0, 0, 3.125, 37.5]


runTestCases()