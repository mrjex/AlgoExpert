# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    finalRange = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array) - 1, finalRange, True)
    searchForRangeHelper(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange


def searchForRangeHelper(array, target, left, right, finalRange, goLeft):
    if left > right:
        return

    mid = (left + right) // 2

    if array[mid] > target:
        return searchForRangeHelper(array, target, left, mid - 1, finalRange, goLeft)
    elif array[mid] < target:
        return searchForRangeHelper(array, target, mid + 1, right, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
                return
            return searchForRangeHelper(array, target, left, mid - 1, finalRange, goLeft)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalRange[1] = mid
                return
            return searchForRangeHelper(array, target, mid + 1, right, finalRange, goLeft)


def runTestCases():
    print("")
    print("")
    print("search-for-range.py:")
    print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45)) # Expected output: [4, 9]
    print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 47)) # Expected output: [-1, -1]
    print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45)) # Expected output: [4, 12]


runTestCases()