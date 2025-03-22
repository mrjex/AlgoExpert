# O(n^2) time | O(n) space
def minimumAreaRectangle(points):
    dictionary = {}
    minRectangleArea = float("inf")

    for i in range(len(points)):
        currentPointString = str(points[i][0]) + ", " + str(points[i][1])
        dictionary[currentPointString] = False

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i][0] != points[j][0] and points[i][1] != points[j][1]:

                point1Coordinates = str(points[i][0]) + ", " + str(points[j][1])
                point2Coordinates = str(points[j][0]) + ", " + str(points[i][1])

                if point1Coordinates in dictionary and point2Coordinates in dictionary:
                    height, width = abs(points[i][1] - points[j][1]), abs(points[i][0] - points[j][0])
                    currentRectangleArea = height * width

                    if currentRectangleArea < minRectangleArea:
                        minRectangleArea = currentRectangleArea

    return 0 if minRectangleArea == float("inf") else minRectangleArea



def runTestCases():
    print(minimumAreaRectangle(
    [
        [1, 5],
        [5, 1],
        [4, 2],
        [2, 4],
        [2, 2],
        [1, 2],
        [4, 5],
        [2, 5],
        [-1, -2]
    ]
    )) # Expected output: 3


    print(minimumAreaRectangle(
    [
        [0, 1],
        [0, 0],
        [2, 1],
        [2, 0],
        [4, 0],
        [4, 1],
        [0, 2],
        [2, 2],
        [4, 2],
        [6, 0],
        [6, 1],
        [6, 2],
        [7, 1],
        [7, 0]
    ]
    )) # Expected output: 1


    print(minimumAreaRectangle(
    [
        [2, 2],
        [3, 2],
        [4, 2]
    ]
    )) # Expected output: 0


runTestCases()