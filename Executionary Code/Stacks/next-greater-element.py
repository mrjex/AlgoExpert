# O(n) time | O(n) space
def nextGreaterElement(array):
    stack = []  # Stack of current possibilities of 'next-greater-element'
    output = [-1 for _ in range(len(array))]

    for counter in reversed(range(len(array) * 2)):
        i = (counter) % len(array)

        # If current element not is smaller than element in stack,
        # it means that the stack-element can't be 'next-greater-element'
        # for the current- as well as the upcoming elements.
        while len(stack) > 0 and array[i] >= stack[-1]:
            stack.pop()
        
        # The elements remaining in the stack are elements with both greater index
        # and greater value than the current element.
        if len(stack) > 0:
            output[i] = stack[-1]
        stack.append(array[i])

    return output

def runTestCases():
    print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2])) # Expected output: [5, 6, 6, 6, 7, -1, 5]
    print(nextGreaterElement([2, 6, 7, 2, 2, 2])) # Expected output: [6, 7, -1, 6, 6, 6]
    print(nextGreaterElement([-8, -1, -1, -2, -4, -5, -6, 0, -9, -91, -2, 8])) # Expected output: [-1, 0, 0, 0, 0, 0, 0, 8, -2, -2, 8, -1]

runTestCases()