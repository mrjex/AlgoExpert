# O(n^2 + m) time | O(n) space
def patternMatcher(pattern, string):
    if len(pattern) == 0 or len(pattern) > len(string):
        return []

    firstLetterA = pattern[0]
    amountOfA = 1
    amountOfB = 0
    firstIdxB = -1

    for i in range(1, len(pattern)):  # O(m)
        if pattern[i] != firstLetterA:
            if firstIdxB == -1:
                firstIdxB = i
            amountOfB += 1
        else:
            amountOfA += 1

    if amountOfB == 0:
        lenA = len(string) / amountOfA
        if lenA % 1 == 0:
            return [string[:int(lenA)], ""] if firstLetterA == "x" else ["", string[:int(lenA)]]
        return []

    else:
        for lenA in range(1, len(string)):  # O(n) time
            lenB = getLenB(lenA, amountOfA, amountOfB, string)
            if lenB == -1:
                continue

            idxB = firstIdxB * lenA
            stringA = string[:lenA]
            stringB = string[idxB: idxB + lenB]
            potentialMatch = "".join(map(lambda char: stringA if char == firstLetterA else stringB, pattern))  # O(2n) = O(n) time
            if potentialMatch == string:
                if firstLetterA == "x":
                    return [stringA, stringB]
                return [stringB, stringA]
        return []


def getLenB(lenA, amountOfA, amountOfB, string):
    v = (len(string) - (amountOfA * lenA)) / amountOfB
    return int(v) if v == int(v) else -1

def runTestCases():
    # Expected Output: ["go", "powerranger"]
    print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))

    # Expected Output: ["powerranger", "go"]
    print(patternMatcher("yyxyyx", "gogopowerrangergogopowerranger"))

    # Expected Output: ["baddaddoomi", "baddaddoom"]
    print(patternMatcher("yxyyyxxy", "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"))

runTestCases()