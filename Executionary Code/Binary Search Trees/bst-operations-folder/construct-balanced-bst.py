# Complexity analysis:
# O(n) time, since we go through all N elements in the array
# O(n) space: Store each element/node in the BST

def minHeightBst(array):
    return minHeightBstHelper(array, None, 0, len(array) - 1)

def minHeightBstHelper(array, bst, left, right):
    if right < left:
        return

    mid = (left + right) // 2
    v = array[mid]

    if bst is None:
        bst = BST(v)
    else:
        bst.insert(v)

    minHeightBstHelper(array, bst, left, mid - 1)
    minHeightBstHelper(array, bst, mid + 1, right)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def runTestCases(): # Takes a sorted array and constructs a balanced BST (with the minimal possible height, so that the nodes are evenly distributed)
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    binarySearchTree = minHeightBst(array)
    printTreeInOrder(binarySearchTree)

def printTreeInOrder(tree):
    if tree is None:
        return

    printTreeInOrder(tree.left)
    print(tree.value)
    printTreeInOrder(tree.right)


# In order traversal while monitoring i:th element
# 'n': number of nodes in tree
# 'k' k:th largest node
# 'i' current iteration
def inOrderTraversalLargestElement(tree, n, k, i, dictionary, array):
    if i is (n - k - 1):
        return
    
    if tree is None:
        return

    # Check if tree.right is None and increment?
    
    inOrderTraversalLargestElement(tree.left, n, k, i, dictionary, array)
    dictionary[i] = tree.value
    i += 1 # Indicate that current element is traversed
    array.append(tree.value)
    # print(str(tree.value) + ", " + str(i))
    inOrderTraversalLargestElement(tree.right, n, k, i, dictionary, array)

    return [tree.value, dictionary, array] # Return the value of the i:th node in an in-order traversal


runTestCases()