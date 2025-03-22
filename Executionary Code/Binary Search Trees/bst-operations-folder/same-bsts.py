from bstOperations import *

# An array of integers is representative of the Binary Search Tree (BST) obtained when inserting each
# integer from left to right into the BST as nodes.

# Only returns true if the two arrays, when inserted in sequence from left to right, equates to identical BSTs, with respect to the BST properties
def sameBsts(arrayOne, arrayTwo): # O(n^2) time & space complexity
    if len(arrayOne) != len(arrayTwo): # Recrusive base case: Two arrays cannot be identical BSTs if the number of nodes deviate
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0: # Base case: Both having the length of 0 makes them inseperable
        return True

    if arrayOne[0] != arrayTwo[0]: # Base case: If the root nodes aren't the same, then it doesn't matter if their child-nodes are identical
        return False

    leftTreeOne, rightTreeOne = getSubTree(arrayOne)
    leftTreeTwo, rightTreeTwo = getSubTree(arrayTwo)

    return sameBsts(leftTreeOne, leftTreeTwo) and sameBsts(rightTreeOne, rightTreeTwo)


# Returns two sub-arrays (left and right) of the current array's first element (root element/node)
def getSubTree(array): # O(n) time & space - Runs n times in the recursive function above:
    rootValue = array[0]
    leftSubtree, rightSubtree = [], []
    
    for i in range(1, len(array)): # Go through all elements in the array
        if array[i] < rootValue: # Left side: x < node.value
            leftSubtree.append(array[i])
        else:
            rightSubtree.append(array[i]) # Right side: x >= node.value

    return leftSubtree, rightSubtree


def runTestCases():
    print("")
    print("")
    print("same-bsts.py:")

    arrayOne_Test1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo_Test1 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    print(sameBsts(arrayOne_Test1, arrayTwo_Test1)) # Expected output: True

    arrayOne_Test2 = [10, 12, 8, 15, 94, 81, 5, 2, 11] # Changed position of 12 and 15, so that 12 becomes its root rather than 15
    arrayTwo_Test2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    print(sameBsts(arrayOne_Test2, arrayTwo_Test2)) # Expected output: False

    arrayOne_Test3 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo_Test3 = [10, 8, 5, 15, 2, 12, 11, 94, 81, 4] # Added an additional element, which invalidates the similarity of the BSTs
    print(sameBsts(arrayOne_Test3, arrayTwo_Test3)) # Expected output: False

    arrayOne_Test4 = [6, 8, 7, 3, 4, 1]
    arrayTwo_Test4 = [6, 3, 1, 4, 8, 7]
    print(sameBsts(arrayOne_Test4, arrayTwo_Test4)) # Expected output: True

    arrayOne_Test5 = [6, 8, 7, 3, 1, 4]
    arrayTwo_Test5 = [6, 3, 4, 1, 8, 7]
    print(sameBsts(arrayOne_Test5, arrayTwo_Test5)) # Expected output: True


runTestCases()