# Complexity analysis:
# O(n) time
# O(n) space
def largestRange(array):
    dictionary = {}
    outArr = [-1, -1]

    for i in range(len(array)):
        dictionary[array[i]] = True

    currentRange = 0
    biggestRange = float("-inf")

    for i in range(len(array)):
        if dictionary[array[i]] == False:
            continue

        leftDigit = array[i] - 1
        rightDigit = array[i] + 1

        while leftDigit in dictionary:  # while leftDigit in dictionary:
            if dictionary[leftDigit] == False:
                break

            dictionary[leftDigit] = False
            leftDigit -= 1
        leftDigit += 1

        while rightDigit in dictionary:  # while rightDigit in dictionary:
            if dictionary[rightDigit] == False:
                break

            dictionary[rightDigit] = False
            rightDigit += 1
        rightDigit -= 1

        currentRange = abs((rightDigit - leftDigit))
        biggestRange = max(biggestRange, currentRange)

        if currentRange == biggestRange:
            outArr = leftDigit, rightDigit

    return outArr

def runTestCases():
    print("")
    print("")
    print("largest-range.py:")

    print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])) # Expected output: [0, 7]
    print(largestRange([-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2])) # Expected output: [-8, 19]

print(runTestCases())