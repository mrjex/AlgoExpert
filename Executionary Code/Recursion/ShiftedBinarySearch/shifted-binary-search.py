# O(log(n)) time | O(1)
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)


def shiftedBinarySearchHelper(array, target, left, right):
    mid = (left + right) // 2

    if left > right:
        return -1
    elif array[mid] == target:
        return mid

    if array[left] <= array[mid]:
        if checkIfTargetIsInInterval(target, array[left], array[mid]):
            return shiftedBinarySearchHelper(array, target, left, mid - 1)
        else:
            return shiftedBinarySearchHelper(array, target, mid + 1, right)
    else:
        if checkIfTargetIsInInterval(target, array[mid], array[right]):
            return shiftedBinarySearchHelper(array, target, mid + 1, right)
        else:
            return shiftedBinarySearchHelper(array, target, left, mid - 1)


def checkIfTargetIsInInterval(target, start, end):
    return target >= start and target <= end


def changePointerValue(pointer, mid):
    if pointer == "RIGHT":
        return mid - 1
    elif pointer == "LEFT":
        return mid + 1


def runTestCases():
    print("")
    print("")
    print("shifted-binary-search.py:")
    print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33)) # Expected output: 8
    print(shiftedBinarySearch([33, 37, 45, 61, 71, 72, 73, 355, 0, 1, 21], 355)) # Expected output: 7
    print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 38)) # Expected output: -1


runTestCases()