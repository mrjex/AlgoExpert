def longestPeak(array):
    longestPeekValue = 0

    for i in range(1, len(array) - 1):
        if array[i - 1] >= array[i] or array[i + 1] >= array[i]:
            continue

        currentPeakValue = 3

        left = i - 2
        right = i + 2

        while left >= 0 and array[left] < array[left + 1]:
            currentPeakValue += 1
            left -= 1

        while right < len(array) and array[right] < array[right - 1]:
            currentPeakValue += 1
            right += 1

        longestPeekValue = max(longestPeekValue, currentPeakValue)
        i = right

    return longestPeekValue


def runTestCases():
    print("")
    print("")
    print("longest-peak.py:")

    print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])) # Expected output: 6
    print(longestPeak([5, 4, 3, 2, 1, 2, 1])) # Expected output: 3

runTestCases()