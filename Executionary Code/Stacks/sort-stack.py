# O(n^2) time - Worst case - When every element strictly is increasing the further down you go in the stack (decreasing array)
# O(n) space
def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)

    insertInorder(stack, top)
    return stack


def insertInorder(stack, currentElement):
    if len(stack) == 0 or currentElement >= stack[-1]:
        stack.append(currentElement)
        return

    top = stack.pop()
    insertInorder(stack, currentElement)

    stack.append(top)


def runTestCases():
    # Expected outputs: Sorted in ascending order
    print(sortStack([-5, 2, -2, 4, 3, 1]))
    print(sortStack([2, 33, 44, 2, -9, -7, -5, -2, -2, -2, 0]))
    print(sortStack([3, 4, 5, 1, 2, 2, 2, 1, 3, 4, 5, 3, 1, 3, -1, 2, 3]))


runTestCases()