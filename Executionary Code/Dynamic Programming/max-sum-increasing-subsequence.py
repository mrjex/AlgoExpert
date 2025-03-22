# python max-sum-increasing-subsequence.py


# Complexity analysis:
# O(n^2) time | O(n) space

# Takes an array and returns a nested array containing the maximal
# possible sum derived from a contained subsequence of elements in
# the inputted array, followed with an array representing that
# particular subsequence
def maxSumIncreasingSubsequence(array):
    maxSums = array[:]
    maxSumIdx = 0
    sequenceChains = [None for _ in range(len(array))]

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] < array[i] and maxSums[j] + array[i] > maxSums[i]:
                maxSums[i] = maxSums[j] + array[i]
                sequenceChains[i] = j
        
        if maxSums[i] > maxSums[maxSumIdx]:
            maxSumIdx = i

    currentIdx = maxSumIdx
    increasingSubsequence = []

    while currentIdx != None:
        increasingSubsequence.append(array[currentIdx])
        currentIdx = sequenceChains[currentIdx]

    return [maxSums[maxSumIdx], list(reversed(increasingSubsequence))]


def runTestCases():
    print("")
    print("")
    print("max-sum-increasing-subsequence.py:")

    arrayTest1 = [10, 70, 20, 30, 50, 11, 30]
    print(maxSumIncreasingSubsequence(arrayTest1)) # Expected output: [110, [10, 20, 30, 50]]

    arrayTest2 = [10, 70, 20, 10, 50, 11, 30]
    print(maxSumIncreasingSubsequence(arrayTest2)) # Expected output: [80, [10, 70]]

runTestCases()