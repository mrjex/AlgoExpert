# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    longestPalindromInterval = [0, 1]

    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)

        # Set the new variable to the array whose difference between the second and first element is the greatest
        greatestCurrentPalindromInterval = max(odd, even, key=lambda x: x[1] - x[0])
        longestPalindromInterval = max(greatestCurrentPalindromInterval, longestPalindromInterval, key=lambda x: x[1] - x[0])

    return string[longestPalindromInterval[0]: longestPalindromInterval[1] + 1]  # Substring max = n characters => O(n) space

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx - 1]


def runTestCases():
    print(longestPalindromicSubstring("abaxyzzyxf")) # Expected Output: xyzzyx
    print(longestPalindromicSubstring("a")) # Expected Output: a
    print(longestPalindromicSubstring("it's highnoon")) # Expected Output: noon
    print(longestPalindromicSubstring("abcdefgfedcba")) # Expected Output: abcdefgfedcba
    print(longestPalindromicSubstring("z234a5abbba54a32z")) # Expected Output: 5abbba5

runTestCases()