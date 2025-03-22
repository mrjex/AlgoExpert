# The average case: O(n + m) time
# O(n) space
# n = length of the main string
# m = length of substring
def underscorifySubstring(string, substring):
    uncorrectedUnderscoreIndexIntervals = getIndexIntervals(string, substring)
    mergedUnderscorePositions = mergeIndexIntervals(uncorrectedUnderscoreIndexIntervals)
    return underscoreify(mergedUnderscorePositions, string)


def getIndexIntervals(string, substring):
    indexIntervals = []
    start = 0
    while True:
        potentialStartIdx = string.find(substring, start)

        if potentialStartIdx != -1:
            start = potentialStartIdx
            indexIntervals.append([start, start + len(substring)])
            start += 1
        else:
            break
    return indexIntervals


def mergeIndexIntervals(uncorrectedUnderscoreIndexIntervals):
    if len(uncorrectedUnderscoreIndexIntervals) == 0:
        return []

    mergedIntervals = []
    currentInterval = uncorrectedUnderscoreIndexIntervals[0]
    nextInterval = currentInterval if len(uncorrectedUnderscoreIndexIntervals) == 1 else uncorrectedUnderscoreIndexIntervals[1]

    for i in range(len(uncorrectedUnderscoreIndexIntervals) - 1):
        currentInterval, nextInterval = uncorrectedUnderscoreIndexIntervals[i], uncorrectedUnderscoreIndexIntervals[i + 1]

        if currentInterval[1] >= nextInterval[0]:
            newInterval = [currentInterval[0], nextInterval[1]]
            uncorrectedUnderscoreIndexIntervals[i + 1] = newInterval
        else:
            mergedIntervals.append(currentInterval)

    if currentInterval[1] >= nextInterval[0]:
        mergedIntervals.append([currentInterval[0], nextInterval[1]])
    else:
        mergedIntervals.append(nextInterval)
    return mergedIntervals


def underscoreify(mergedUnderscorePositions, string):
    underscoreifiedChars = []

    x = 0
    i = 0
    while i < len(string):
        if x < len(mergedUnderscorePositions) and i == mergedUnderscorePositions[x][0]:
            underscoreifiedChars.append("_" + string[mergedUnderscorePositions[x][0] : mergedUnderscorePositions[x][1]] + "_")
            i += mergedUnderscorePositions[x][1] - mergedUnderscorePositions[x][0]
            x += 1
        else:
            underscoreifiedChars.append(string[i])
            i += 1

    return "".join(underscoreifiedChars)

def runTestCases():
    # Expected Output: "_test_this is a _testtest_ to see if _testestest_ it works"
    print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))

    # Expected Output: "this is a test to see if it works and test"
    print(underscorifySubstring("this is a test to see if it works and test", "mytest"))

    # Expected Output: "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b_aaa_bb_a_b_a_b_aa_"
    print(underscorifySubstring("abababababababababababababaababaaabbababaa", "a"))

    # Expected Output: "_abcabcabcabcabcabcabcabcabcabcabcabcabcabc_"
    print(underscorifySubstring("abcabcabcabcabcabcabcabcabcabcabcabcabcabc", "abc"))

runTestCases()
