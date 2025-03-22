# O(n) time | O(n) space - n is the length of the input-string
def longestSubstringWithoutDuplication(string):
    if len(string) == 0:
        return ""

    currentDictionary = {}
    greatestSubstringInterval = [0, 0]
    start = 0

    for i, character in enumerate(string):
        if character in currentDictionary:
            currentSubstringInterval = [start, i]
            greatestSubstringInterval = updateGreatestSubstringInterval(currentSubstringInterval, greatestSubstringInterval)

            start = currentDictionary[character] + 1
            currentDictionary.clear()

            for j in range(start, i):
                currentDictionary[string[j]] = j

        currentDictionary[character] = i

    currentSubstringInterval = [start, len(string)]
    greatestSubstringInterval = updateGreatestSubstringInterval(currentSubstringInterval, greatestSubstringInterval)

    return string[greatestSubstringInterval[0]:greatestSubstringInterval[1]]


def updateGreatestSubstringInterval(current, greatest):
    return max(greatest, current, key=lambda element: element[1] - element[0])

def runTestCases():
    # Expected Output: mentisac
    print(longestSubstringWithoutDuplication("clementisacap"))

    # Expected Output: defcTESG
    print(longestSubstringWithoutDuplication("abcdeabcdefcTESGTJ"))

    # Expected Output: cbde
    print(longestSubstringWithoutDuplication("abcbde"))

runTestCases()