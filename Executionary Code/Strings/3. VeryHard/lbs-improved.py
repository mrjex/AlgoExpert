# O(n) time | O(n) space
def longestBalancedSubstring(string):
    stack = []
    stack.append(-1)
    greatestLength = 0
    
    for i, char in enumerate(string):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                currentLength = i - stack[-1]
                greatestLength = max(greatestLength, currentLength)
    return greatestLength

def runTestCases():
    print(longestBalancedSubstring("(()))(")) # Expected Output: 4
    print(longestBalancedSubstring("((()))()()()()()()()()()()")) # Expected Output: 26
    print(longestBalancedSubstring("(((((((((((((((((()")) # Expected Output: 2

runTestCases()