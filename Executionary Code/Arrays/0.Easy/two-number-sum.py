# Time complexity: O(n * log(n) + n) = O(n* log(n))
def twoNumberSumInefficient(array, targetSum):
    array = sorted(array) # O(n *log(n))
    i = 0
    j = len(array) - 1
    current_sum = 0

    while i < j: # O(n)
        current_sum = array[i] + array[j]

        if current_sum > targetSum:
            j -= 1
        elif current_sum < targetSum:
            i += 1
        else:
            return [array[i], array[j]]

    return []


# Time complexity: O(n)
def twoNumberSumEfficient(array, targetSum):
    myDictionary = {}
    for current in array:
        y = targetSum - current
        if y in myDictionary: # Search for a value with the key 'y' within the dictionary: O(1) operation
            return [y, current]
        else:
            myDictionary[current] = False
    return []

def runTestCases():
    print("")
    print("")
    print("two-number-sum.py:")

    print(twoNumberSumInefficient([3, 5, -4, 8, 11, 1, -1, 6], 10)) # Expected output: [-1, 11]
    print(twoNumberSumEfficient([8, 4, 9, 2, 53], 10)) # Expected output: [8, 2]
    print(twoNumberSumEfficient([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163)) # Expected output: [210, -47]

runTestCases()