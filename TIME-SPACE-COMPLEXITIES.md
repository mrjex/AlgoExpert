# Time & Space Complexities


## Arrays

A collection of array manipulation problems with varying complexity levels.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Two Number Sum | Easy | O(n) | O(n) |
| Three Number Sum | Medium | O(n²) | O(n) |
| Smallest Difference | Medium | O(n log n + m log m) | O(1) |
| Move Element To End | Medium | O(n) | O(1) |
| Monotonic Array | Medium | O(n) | O(1) |
| Spiral Traverse | Medium | O(n) | O(n) |
| Longest Peak | Medium | O(n) | O(1) |

### Featured Solution: Two Number Sum

```python
# O(n) time | O(n) space
def twoNumberSumEfficient(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
```

## Binary Search Trees

Implementation of tree traversal algorithms and tree-based data structures.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| BST Construction | Medium | O(log n) average | O(log n) average |
| Validate BST | Medium | O(n) | O(h) |
| BST Traversal | Medium | O(n) | O(n) |
| Min Height BST | Medium | O(n) | O(n) |

## Dynamic Programming

Complex problems solved using optimal substructure and overlapping subproblems.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Max Subset Sum No Adjacent | Medium | O(n) | O(1) |
| Number of Ways to Make Change | Medium | O(nd) | O(n) |
| Levenshtein Distance | Medium | O(nm) | O(nm) |
| Min Number of Coins For Change | Medium | O(nd) | O(n) |
| Max Sum Increasing Subsequence | Hard | O(n²) | O(n) |
| Longest Common Subsequence | Hard | O(nm) | O(nm) |

### Featured Solution: Levenshtein Distance

The Levenshtein distance algorithm measures the minimum number of single-character operations (insertions, deletions, or substitutions) required to change one string into another.

```python
# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    edits = [[j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    
    for i in range(1, len(str1) + 1):
        edits[i][0] = edits[i-1][0] + 1
        
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])
                
    return edits[-1][-1]
```

## Graphs

Network and traversal problems modeled using graph data structures.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Depth-First Search | Easy | O(V + E) | O(V) |
| Breadth-First Search | Medium | O(V + E) | O(V) |
| River Sizes | Medium | O(wh) | O(wh) |
| Youngest Common Ancestor | Medium | O(d) | O(1) |

## Greedy Algorithms

Solving optimization problems by making locally optimal choices at each stage.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Minimum Waiting Time | Easy | O(n log n) | O(1) |
| Class Photos | Easy | O(n log n) | O(1) |
| Tandem Bicycle | Easy | O(n log n) | O(1) |
| Task Assignment | Medium | O(n log n) | O(n) |

## Recursion

Implementing elegant solutions to problems that can be defined in terms of similar subproblems.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Nth Fibonacci | Easy | O(n) | O(1) |
| Product Sum | Easy | O(n) | O(d) |
| Permutations | Medium | O(n*n!) | O(n*n!) |
| Powerset | Medium | O(n*2ⁿ) | O(n*2ⁿ) |

## Stacks

Implementations leveraging Last-In-First-Out data structures.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Min Max Stack Construction | Medium | O(1) | O(n) |
| Balanced Brackets | Medium | O(n) | O(n) |
| Sunset Views | Medium | O(n) | O(n) |

## Strings

Text processing algorithms and string manipulation.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Palindrome Check | Easy | O(n) | O(1) |
| Caesar Cipher Encryptor | Easy | O(n) | O(n) |
| Longest Palindromic Substring | Medium | O(n²) | O(n) |
| Group Anagrams | Medium | O(w * n * log n) | O(wn) |