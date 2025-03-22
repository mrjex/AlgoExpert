# This program calulcates the number of ways to traverse the graph given two
# parameters: width and height. The traversal is only supported by down and
# right movements. In other words, the starting point of the graph is always
# top-left and ends at bottom-right.


# O(2^(n + m)) time | O(n + m) space
def numberOfWaysToTraverseGraphRecursive(width, height):
    if width == 1 or height == 1:
        return 1

    return numberOfWaysToTraverseGraphRecursive(width - 1, height) + numberOfWaysToTraverseGraphRecursive(width, height - 1)


# O(wh) time | O(wh) space
def numberOfWaysToTraverseGraphIterative(width, height): # Dynamic Programming
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(width):
        for j in range(height):
            if j == 0 or i == 0:
                grid[j][i] = 1
            else:
                grid[j][i] = grid[j][i - 1] + grid[j - 1][i]

    return grid[-1][-1]


def runTestCases():
    print("")
    print("")
    print("traverse-graph.py:")

    print(numberOfWaysToTraverseGraphRecursive(4, 3)) # Expected output: 10
    print(numberOfWaysToTraverseGraphRecursive(3, 4)) # Expected output: 10
    print(numberOfWaysToTraverseGraphRecursive(6, 1)) # Expected output: 1
    print(numberOfWaysToTraverseGraphRecursive(6, 2)) # Expected output: 6

    print(numberOfWaysToTraverseGraphIterative(2, 2)) # Expected output: 2
    print(numberOfWaysToTraverseGraphIterative(8, 3)) # Expected output: 36
    print(numberOfWaysToTraverseGraphIterative(2, 5)) # Expected output: 5


runTestCases()