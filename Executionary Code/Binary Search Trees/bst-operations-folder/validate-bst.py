# from 'classname' import *
# from 'foldername'.'classname' import *

from bstOperations import *


# O(n) time | O(d) space
# n is the amount of nodes in the BST tree
# d is the depth of the tree: the longest existing branch
# If the tree only has one branch n = d <=> O(n) space

# The parameters 'currentMin' and currentMax' represent the current numerical constraints of a
# node, based on the traversal from the root to the current sub-branch
def validateBst(tree, currentMin=float("-inf"), currentMax=float("inf")):
    if tree is None: # If all elements traversed and no method returned false, then return true
        return True
    
    if tree.value >= currentMax or tree.value < currentMin: # If the current node violates the BST property, return false
        return False
    
    # If left sub branch and right sub branch are within boundaries, return true:
    #   * traversing to left: Update max boundary
    #   * traversing to right: Update min boundary
    return validateBst(tree.left, currentMin, tree.value) and validateBst(tree.right, tree.value, currentMax)

def runTestCases():
    print("")
    print("")
    print("validate-bst.py:")

    print(validateBst(createInvalidBST(), float("-inf"), float("inf"))) # Expected output: False
    print(validateBst(createValidBST(), float("-inf"), float("inf"))) # Expected output: True


def createInvalidBST():
    binarySearchTree = BST(10)

    # Insert left-sub-tree nodes
    binarySearchTree.insert(5)
    binarySearchTree.insert(2)
    binarySearchTree.insert(1)
    binarySearchTree.insert(5)


    # Insert right-sub-tree nodes
    binarySearchTree.insert(15)
    binarySearchTree.insert(13)
    binarySearchTree.insert(22)
    binarySearchTree.insert(14)

    ## Add a node that violates the BST propety
    invalidNode = BST(9)
    # print(binarySearchTree.right.right.value) # 22
    binarySearchTree.right.right. right = invalidNode

    return binarySearchTree


def createValidBST():
    binarySearchTree = BST(10)

    # Insert left-sub-tree nodes
    binarySearchTree.insert(5)
    binarySearchTree.insert(2)
    binarySearchTree.insert(1)
    binarySearchTree.insert(5)


    # Insert right-sub-tree nodes
    binarySearchTree.insert(15)
    binarySearchTree.insert(13)
    binarySearchTree.insert(22)
    binarySearchTree.insert(14)

    return binarySearchTree


runTestCases()