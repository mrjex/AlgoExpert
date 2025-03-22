# Time complexity:
# O(n^2) time
# O(n^2) space
def fourNumberSum(array, targetSum):
    outArr = []
    pairs = {}

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            y = targetSum - currentSum

            if y in pairs:
                for currentPair in pairs[y]:
                    outArr.append([currentPair[0], currentPair[1], array[i], array[j]])

        for a in range(0, i):
            currentSum = array[a] + array[i]

            if currentSum not in pairs:
                pairs[currentSum] = [[array[a], array[i]]]
            else:
                pairs[currentSum].append([array[a], array[i]])

    return outArr


def runTestCases():
    print("")
    print("")
    print("four-number-sum.py:")

    print(fourNumberSum([7, 6, 4, -1, 1, 2], 16)) # Expected output: [[7, 6, 4, -1], [7, 6, 1, 2]]

    print(fourNumberSum([-1, 22, 18, 4, 7, 11, 2, -5, -3], 30))
    # Expected output:
    # [
    #    [-1, 22, 7, 2],
    #    [22, 4, 7, -3],
    #    [-1, 18, 11, 2],
    #    [18, 4, 11, -3],
    #    [22, 11, 2, -5]
    # ]

runTestCases()