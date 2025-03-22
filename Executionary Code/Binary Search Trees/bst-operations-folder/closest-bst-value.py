# Worst Case: O(n) --> If all elements are either strictly greater or smaller than each other,
# such that the tree becomes a line rather than a branching tree

# Average Case: O(log(n)) --> Assuming the nodes are evenly distributed

def findClosestValueInBst(tree, target):
    currentNode = tree # Set initial node to root of the inputted tree
    closestNode = tree.value

    # Variables for keeping track of the tree height of the closest node so that we can return it
    currentNodeHeightLevel = 0 # If the closest node isn't the target node, then we need to activaly store the height during the iteration as we search
    treeHeightLevel = 0

    while currentNode is not None:
        if abs(target - currentNode.value) <= abs(target - closestNode): # Compare current node's range versus the closest one found yet throughout the tree-traversal
            closestNode = currentNode.value
            currentNodeHeightLevel = treeHeightLevel

        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break
        
        treeHeightLevel += 1

    return [closestNode, currentNodeHeightLevel] # Returns the closest node and its height-level in the BST


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def createTree():
    root = BST(10)

    # Declare nodes for left-side of root node
    a = BST(5)
    b = BST(2)
    c = BST(1)
    d = BST(5)

    # Declare right-side nodes
    e = BST(15)
    f = BST(13)
    g = BST(22)
    h = BST(14)

    # Create connections/edges of the Binary Search Tree
    root.left = a
    root.right = e

    a.left = b
    a.right = d

    b.left = c

    e.left = f
    e.right = g

    f.right = h

    return root


def runTestCases():
    outputA = findClosestValueInBst(createTree(), 11)
    print(str(outputA[0]) + ", " + str(outputA[1])) # Expected output: [10, 0]

    outputB = findClosestValueInBst(createTree(), 14)
    print(str(outputB[0]) + ", " + str(outputB[1])) # Expected output: [14, 3]

    outputC = findClosestValueInBst(createTree(), 3)
    print(str(outputC[0]) + ", " + str(outputC[1])) # Expected output: [2, 2]

    outputD = findClosestValueInBst(createTree(), 6)
    print(str(outputD[0]) + ", " + str(outputD[1])) # Expected output: [5, 2]


runTestCases()