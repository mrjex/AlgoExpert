# Brute force solution
# O(n^3) time | O(n) space
def longestBalancedSubstring(string):
    greatestLength = 0
    for i in range(len(string)):  # O(n) time
        endIteration = False
        for j in range(i + 1, len(string), 2):  # O(n) time
            currentString = string[i: j + 1]
            stack = []

            for char in currentString:  # O(n) time
                if char == "(":
                    stack.append(char)
                elif len(stack) == 0:
                    endIteration = True
                    break
                else:
                    stack.pop()

            if endIteration:
                break

            if len(stack) == 0:
                greatestLength = max(greatestLength, j + 1 - i)
    return greatestLength

def runTestCases():
    print(longestBalancedSubstring("(()))(")) # Expected Output: 4
    print(longestBalancedSubstring("((()))()()()()()()()()()()")) # Expected Output: 26
    print(longestBalancedSubstring("(((((((((((((((((()")) # Expected Output: 2

runTestCases()