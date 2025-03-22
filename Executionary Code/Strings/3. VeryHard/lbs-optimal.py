# O(n) time | O(1) space
def longestBalancedSubstring(string):
    i = 0
    state = "increment"
    greatestLength = 0

    opening, closing = resetParenthesisValues()

    while i < len(string):
        if string[i] == "(":
            opening += 1
        else:
            closing += 1

        if state == "increment" and closing > opening:
            opening, closing = resetParenthesisValues()
        elif state == "decrement" and opening > closing:
            opening, closing = resetParenthesisValues()
        elif opening == closing:
            greatestLength = max(greatestLength, opening + closing)

        i = updateIdxValue(state, i)

        if i == len(string):
            state = "decrement"
            i -= 1
            opening, closing = resetParenthesisValues()
        elif i == -1:
            break
    return greatestLength


def updateIdxValue(state, idx):
    return idx + 1 if state == "increment" else idx - 1

def resetParenthesisValues():
    return [0, 0]

def runTestCases():
    print(longestBalancedSubstring("(()))(")) # Expected Output: 4
    print(longestBalancedSubstring("((()))()()()()()()()()()()")) # Expected Output: 26
    print(longestBalancedSubstring("(((((((((((((((((()")) # Expected Output: 2

runTestCases()