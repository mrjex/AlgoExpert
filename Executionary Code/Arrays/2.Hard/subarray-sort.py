# O(n) time | O(1) space
def subarraySort(array):
    smallestUnsortedNumber = float("inf")
    biggestUnsortedNumber = float("-inf")

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            smallestUnsortedNumber = min(smallestUnsortedNumber, array[i - 1], array[i])
            biggestUnsortedNumber = max(biggestUnsortedNumber, array[i - 1], array[i])

    if biggestUnsortedNumber == float("-inf"):
        return [-1, -1]

    leftIdx = 0
    while array[leftIdx] <= smallestUnsortedNumber:
        leftIdx += 1

    rightIdx = len(array) - 1
    while array[rightIdx] >= biggestUnsortedNumber:
        rightIdx -= 1

    return [leftIdx, rightIdx]

def runTestCases():
    print("")
    print("")
    print("subarray-sort.py:")

    print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])) # Expected output: [3, 9]
    print(subarraySort([1, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11])) # Expected output: [6, 7]

runTestCases()