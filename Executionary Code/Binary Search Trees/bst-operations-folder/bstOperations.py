class BST: # Binary Search Tree class with supportive functions
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, nodeToInsert):
        currentNode = self # Initially set the node to the root of the Binary Search Tree

        while True:
            if nodeToInsert >= currentNode.value:
                if currentNode.right is None: # If no node is at the current location, we can insert the desired value in the tree
                    currentNode.right = BST(nodeToInsert)
                    break
                else:
                    currentNode = currentNode.right # Traverse the tree to the right
            elif nodeToInsert < currentNode.value:
                if currentNode.left: # If the current node has a left child node, traverse to it
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(nodeToInsert) # If no child was found, then we insert
                    break
        return self

    def contains(self, targetNode): # O(log(n)) time, since an evenly distributed BST would imply that we divide the number of potential output-nodes by 2 for each iteration
        currentNode = self

        while currentNode is not None:
            if targetNode > currentNode.value:
                currentNode = currentNode.right
            elif targetNode < currentNode.value:
                currentNode = currentNode.left
            else:
                return True # Return the first node-instance that has the same value as the target value
        return False


    def remove(self, nodeToRemove, parentNode=None):
        currentNode, parentNode = self.getNodeAndParent(nodeToRemove, parentNode)

        if currentNode == None:  # The node to remove wasn't found: Don't remove anything and return the tree without modifying it
            return

        if parentNode == None and currentNode.left == None and currentNode.right == None:  # nodeToRemove is the root node that is the only node in the tree: Return an empty tree
            return

        if currentNode.left and currentNode.right:
            replacementNode = currentNode.right.getMinNode(parentNode) # Get minimal node in right subtree
            currentNode.value = replacementNode.value
            currentNode.right.remove(replacementNode.value, currentNode)

        elif currentNode.left is None and currentNode.right is None: # Case: Delete leaf nodes and disconnect from parent
            if parentNode.right == currentNode:
                parentNode.right = None # Disconnect/Delete leaf node
            elif parentNode.left == currentNode:
                parentNode.left = None # Disconnect/Delete leaf node

        elif currentNode.left:  # The node to remove only has a left child-branch
            replacementNode = currentNode.left.getMaxNode(parentNode)
            currentNode.value = replacementNode.value
            currentNode.left.remove(replacementNode.value, currentNode)

        elif currentNode.right:
            replacementNode = currentNode.right.getMinNode(parentNode)
            currentNode.value = replacementNode.value
            currentNode.right.remove(replacementNode.value, currentNode)

        return self

    def getMaxNode(self, parentNode):
        currentNode = self
        while currentNode.right:
            parentNode = currentNode
            currentNode = currentNode.right
        return currentNode

    # Invoked with {node}.right, since we use this function to find the minimal node in the right subtree
    def getMinNode(self, parentNode): # Get left-most (minimal BST node) in a sub-tree
        currentNode = self
        while currentNode.left:
            parentNode = currentNode
            currentNode = currentNode.left
        return currentNode


    def getNodeAndParent(self, targetNode, parentNode=None):
        currentNode = self

        while currentNode is not None:
            if currentNode.value == targetNode:
                return currentNode, parentNode
            
            parentNode = currentNode

            if currentNode.value > targetNode:
                # parentNode = currentNode
                currentNode = currentNode.left
            else:
                # parentNode = currentNode
                currentNode = currentNode.right

        return None, None # Indicate that no node with the target value exists and that it has no parent in the BST

def createTree():
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

def runTestCases():
    print("")
    print("")
    print("bstOperations.py:")

    binarySearchTree = createTree()

    binarySearchTree.insert(12) # Expected relation to root: root.right.left.left
    print(binarySearchTree.right.left.left.value) # Expected output: 12

    print(binarySearchTree.contains(0)) # Expected output: False

    binarySearchTree.insert(0) # Expected relation to root: root.left.left.left.left
    print(binarySearchTree.left.left.left.left.value) # Expected output: 0

    print(binarySearchTree.contains(0)) # Expected output: True

    binarySearchTree.remove(12, None)
    print(binarySearchTree.contains(12)) # Expected output: False


runTestCases()
