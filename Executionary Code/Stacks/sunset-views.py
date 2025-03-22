# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    if direction == "EAST":
        i = len(buildings) - 1
        endIdx = -1
    else:
        i = 0
        endIdx = len(buildings)

    minHeightAllowed = float("-inf")
    buildingsWithSunsetViews = []

    while i != endIdx:  # O(n) time
        if buildings[i] >= minHeightAllowed:
            buildingsWithSunsetViews.append(i)
            minHeightAllowed = buildings[i] + 1

        if direction == "EAST":
            i -= 1
        else:
            i += 1

    if direction == "EAST":
        s, e = 0, len(buildingsWithSunsetViews) - 1
        while s < e:  # O(0,5n) <=> O(n) time
            buildingsWithSunsetViews[s], buildingsWithSunsetViews[e] = buildingsWithSunsetViews[e], buildingsWithSunsetViews[s]
            s += 1
            e -= 1

    return buildingsWithSunsetViews

def runTestCases():
    print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST")) # Expected output: [1, 3, 6, 7]
    print(sunsetViews([7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5], "EAST")) # Expected output: [4, 5, 6, 7, 11]
    print(sunsetViews([1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8], "WEST")) # Expected output: [0, 1, 2, 4, 5, 6, 10, 13]

runTestCases()
