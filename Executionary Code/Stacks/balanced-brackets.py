# O(n) time | O(n) space
def balancedBrackets(string):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for currentBracket in string:
        if currentBracket == "(" or currentBracket == "[" or currentBracket == "{":
            stack.append(currentBracket)
        elif currentBracket in pairs:
            if len(stack) == 0:
                return False
            elif pairs[currentBracket] != stack[-1]:
                return False
            stack.pop()

    return len(stack) == 0

def runTestCases():
    print(balancedBrackets("([])(){}(())()()")) # Expected output: True
    print(balancedBrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))")) # Expected output: False
    print(balancedBrackets("{}()")) # Expected output: True
    print(balancedBrackets("(()agwg())((()agwga()())gawgwgag)")) # Expected output: True
    print(balancedBrackets("(agwgg)([ghhheah%&@Q])")) # Expected output: True


runTestCases()