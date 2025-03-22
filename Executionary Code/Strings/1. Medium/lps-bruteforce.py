# Brute-force approach: O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    longest = string[0]

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            currentString = string[i:j+1]
            if len(currentString) > len(longest) and isPalindrome(currentString):
                longest = currentString
    return longest

def isPalindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def runTestCases():
    print(longestPalindromicSubstring("abaxyzzyxf")) # Expected Output: xyzzyx
    print(longestPalindromicSubstring("a")) # Expected Output: a
    print(longestPalindromicSubstring("it's highnoon")) # Expected Output: noon
    print(longestPalindromicSubstring("abcdefgfedcba")) # Expected Output: abcdefgfedcba
    print(longestPalindromicSubstring("z234a5abbba54a32z")) # Expected Output: 5abbba5

runTestCases()