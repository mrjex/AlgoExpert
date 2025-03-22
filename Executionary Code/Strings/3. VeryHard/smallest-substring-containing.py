# b - length of bigString
# s - length of smallString
# O(2s + 2b) = O(2(b + s)) = O(b + s) time | O(b + s) space
def smallestSubstringContaining(bigString, smallString):
    targetCharAmounts = {}
    for char in smallString:  # O(s) time
        increaseCharAmount(targetCharAmounts, char)
    currentAmounts = targetCharAmounts.copy()
    for key in currentAmounts:  # O(s) time
        currentAmounts[key] = 0

    leftIdx, rightIdx = 0, 0
    substringBounds = [0, float("inf")]

    amountOfApprovedChars = 0
    maxApprovedChars = len(targetCharAmounts.keys())

    while rightIdx < len(bigString):  # O(b) time
        rightChar = bigString[rightIdx]
        if rightChar not in targetCharAmounts:
            rightIdx += 1
            continue

        increaseCharAmount(currentAmounts, rightChar)
        if currentAmounts[rightChar] == targetCharAmounts[rightChar]:
            amountOfApprovedChars += 1

        rightIdx += 1
        while amountOfApprovedChars == maxApprovedChars and leftIdx <= rightIdx:  # O(b) time
            substringBounds = min(substringBounds, [leftIdx, rightIdx], key=lambda x: x[1] - x[0])
            leftChar = bigString[leftIdx]

            if leftChar not in targetCharAmounts:
                leftIdx += 1
                continue

            currentAmounts[leftChar] -= 1
            if currentAmounts[leftChar] < targetCharAmounts[leftChar]:
                amountOfApprovedChars -= 1
            leftIdx += 1

    return bigString[substringBounds[0]: substringBounds[1]] if substringBounds[1] != float("inf") else ""


def increaseCharAmount(charAmount, key):
    if key not in charAmount:
        charAmount[key] = 0
    charAmount[key] += 1

def runTestCases():
    # Expected Output: "f$axb$"
    print(smallestSubstringContaining("abcd$ef$axb$c$", "$$abf"))

    # Expected Output: "affa+a$Affab+a+a+$a"
    print(smallestSubstringContaining("a$fuu+afff+affaffa+a$Affab+a+a+$a$bccgtt+aaaacA+++aaa$", "a+$aaAaaaa$++"))

    # Expected Output: ""
    print(smallestSubstringContaining("14562435612!88281932363365$412356789901", "#!333333123!"))

    # Expected Output: "#z2!"
    print(smallestSubstringContaining("14562435612z!8828!193236!336!5$41!23!5!6789901#z2!", "#!2z"))

runTestCases()
