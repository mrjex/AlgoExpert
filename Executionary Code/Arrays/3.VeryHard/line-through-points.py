# Solution based on the kValue between p1 and p2
# O(n^2) time | O(n) space
def lineThroughPoints(points):
    maxNumberOfPointsOnLine = 1

    for i in range(len(points)):
        kValuesToCurrentPoint = {}

        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            k = str(getKValueBetweenPoints(p1, p2))

            if k not in kValuesToCurrentPoint:
                kValuesToCurrentPoint[k] = 1

            kValuesToCurrentPoint[k] += 1

        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(kValuesToCurrentPoint.values(), default=1))

    return maxNumberOfPointsOnLine

def getKValueBetweenPoints(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2

    if p1x == p2x:
        return float("inf")

    x2, x1 = p1x, p2x
    y2, y1 = p1y, p2y

    if p2x > p1x:
        x2, x1 = p2x, p1x
        y2, y1 = p2y, p1y

    k = (y2 - y1) / (x2 - x1)
    return k


def runTestCases():
    print(lineThroughPoints(
    [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1]
    ])) # Expected output: 4

    print(lineThroughPoints(
    [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 1],
        [3, 2],
        [3, 4],
        [3, 5],
        [4, 1],
        [4, 2],
        [4, 3],
        [4, 4],
        [4, 5],
        [5, 1],
        [5, 2],
        [5, 3],
        [5, 4],
        [5, 5],
        [6, 6],
        [2, 6]
    ]
    )) # Expected output: 6

    print(lineThroughPoints(
    [
        [-78, -9],
        [67, 87],
        [46, 87],
        [4, 5],
        [9, 83],
        [34, 47]
    ]
    )) # Expected output: 2


runTestCases()
