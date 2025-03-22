# O(nm) time | O(min(n, m)) space
#   * n = str1
#   * m = str2

# APPROACH: Store only 2 rows at a time (current, previous) to access the new value for the current field in the 2D-array

# Assigning the current field in the 2D-array to...
#   - Its `left upper diagonal value`, is the same thing as not performing any additional edit-operations to include the
#     `row-substring` in the `column-substring`
#
#   - The minimal value of its 3 neighbouring fields added by one, translates to finding the minimal amount of edit-operations
#     needed to build the substring without the current letter and then registering an additional operation to construct the new substring


# Returns an integer representative of the minimum number of operations
# (insert letter, substitute letter, deletion of letter), that is required
# for the strings to be identical.
def levenshteinDistance(str1, str2):
    smallStr = str1 if len(str1) < len(str2) else str2
    bigStr = str1 if len(str1) >= len(str2) else str2

    evenRow = [a for a in range(len(smallStr) + 1)]
    oddRow = [float("inf") for a in range(len(smallStr) + 1)]

    for r in range(1, len(bigStr) + 1):
        if r % 2 == 0:
            currentRow = evenRow
            previousRow = oddRow
        else:
            currentRow = oddRow
            previousRow = evenRow

        currentRow[0] = r

        for c in range(1, len(smallStr) + 1):
            if bigStr[r - 1] == smallStr[c - 1]:
                currentRow[c] = previousRow[c - 1]
            else:
                currentRow[c] = 1 + min(previousRow[c - 1], previousRow[c], currentRow[c - 1])

    return evenRow[-1] if len(bigStr) % 2 == 0 else oddRow[-1]

def runTestCases():
    print("")
    print("")
    print("levensthein-distance.py:")

    str1_Test1 = "abc"
    str2_Test1 = "yabd"
    print(levenshteinDistance(str1_Test1, str2_Test1)) # Expected output: 2 (insert "y" and substitute "c" for "d")

    str1_Test2 = "Hello"
    str2_Test2 = "HelloA"
    print(levenshteinDistance(str1_Test2, str2_Test2)) # Expected output: 1 (Delete "A")

    str1_Test3 = "Programmer"
    str2_Test3 = "Pr0grannerB"
    print(levenshteinDistance(str1_Test3, str2_Test3)) # Expected output: 4 (Sub '0' for '0', sub 'm' for 'n' twice, delete 'B')


runTestCases()