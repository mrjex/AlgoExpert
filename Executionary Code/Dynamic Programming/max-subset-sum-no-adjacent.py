def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    cMV = [array[0], max(array[0], array[1])]  # cMV = currentMaxValues

    for i in range(2, len(array)):
        tempVal = cMV[1]
        cMV[1] = max(cMV[0] + array[i], cMV[1])
        cMV[0] = tempVal

    return cMV[1]

def runTestCases():
    print("")
    print("")
    print("max-subset-sum-no-adjacent.py:")

    print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])) # Expected Output: 330
    print(maxSubsetSumNoAdjacent([])) # Expected Output: 0
    print(maxSubsetSumNoAdjacent([4, 3, 5, 200, 5, 3])) # Expected Output: 207
    print(maxSubsetSumNoAdjacent([125, 210, 250, 120, 150, 300])) # Expected Output: 675


runTestCases()