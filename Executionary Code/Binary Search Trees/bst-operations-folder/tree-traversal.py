from bstOperations import *

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


def runTestCases():
    print("")
    print("")
    print("tree-traversal.py:")

    # Import a Binary Search Tree created in 'bstOperations.py'
    importedBST = createTree()

    inOrderArr = []
    inOrderTraverse(importedBST, inOrderArr)

    print("In Order:")
    for element in inOrderArr: # Expected output: [1, 2, 2, 5, 5, 10, 13, 14, 15, 22] (The order of elements should always be in ascending order)
        print(element)

    print("")
    
    preOrderArr = []
    preOrderTraverse(importedBST, preOrderArr)

    print("Pre Order:")
    for element in preOrderArr: # Expected output: [1, 2, 2, 5, 5, 10, 13, 14, 15, 22] (The order of elements should always be in ascending order)
        print(element)
    
    print("")
    
    postOrderArr = []
    postOrderTraverse(importedBST, postOrderArr)

    print("Post Order:")
    for element in postOrderArr: # Expected output: [1, 2, 2, 5, 5, 10, 13, 14, 15, 22] (The order of elements should always be in ascending order)
        print(element)


runTestCases()
