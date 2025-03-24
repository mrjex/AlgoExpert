# AlgoExpert 🧠

> A Comprehensive Collection of Algorithm & Data Structure Implementations with Automated Testing

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![C#](https://img.shields.io/badge/C%23-.NET-purple)](https://dotnet.microsoft.com/languages/csharp)
[![Bash](https://img.shields.io/badge/Bash-Script-green)](https://www.gnu.org/software/bash/)
[![AlgoExpert](https://img.shields.io/badge/Practice-AlgoExpert-orange)](https://www.algoexpert.io/)

## 📑 Table of Contents

- [AlgoExpert 🧠](#algoexpert-)
  - [📑 Table of Contents](#-table-of-contents)
  - [🎯 Overview](#-overview)
  - [📂 Repository Structure](#-repository-structure)
  - [🧮 Algorithm Implementations](#-algorithm-implementations)
    - [Arrays](#arrays)
      - [Featured Solution: Two Number Sum](#featured-solution-two-number-sum)
    - [Binary Search Trees](#binary-search-trees)
    - [Dynamic Programming](#dynamic-programming)
      - [Featured Solution: Levenshtein Distance](#featured-solution-levenshtein-distance)
    - [Graphs](#graphs)
    - [Greedy Algorithms](#greedy-algorithms)
    - [Recursion](#recursion)
    - [Stacks](#stacks)
    - [Strings](#strings)
  - [🔄 Automated Testing](#-automated-testing)
    - [Test Automation in Action](#test-automation-in-action)
  - [🚀 Running the Code](#-running-the-code)
    - [Prerequisites](#prerequisites)
    - [Execution Steps](#execution-steps)

## 🎯 Overview

This repository documents my algorithmic journey, showcasing implementations of various data structures and algorithms. Initially developed in Summer 2022 to refine my problem-solving skills, this collection has grown to encompass a wide range of computational challenges across multiple programming languages.

Each implementation includes:
- ✅ Optimized algorithm solutions
- ✅ Time & space complexity analysis
- ✅ Multiple approaches where applicable
- ✅ Test cases verifying correctness
- ✅ Visual explanations of complex concepts

## 📂 Repository Structure

```
AlgoExpert/
├── Executionary Code/          # Algorithm implementations
│   ├── Arrays/
│   ├── Binary Search Trees/
│   ├── Dynamic Programming/
│   ├── Graphs/
│   ├── Greedy Algorithms/
│   ├── Recursion/
│   ├── Stacks/
│   └── Strings/
├── Test Outputs/               # Automated test results
├── run.sh                      # Automation script
└── README.md                   # Project documentation
```

## 🧮 Algorithm Implementations

### Arrays

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

#### Featured Solution: Two Number Sum

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

### Binary Search Trees

Implementation of tree traversal algorithms and tree-based data structures.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| BST Construction | Medium | O(log n) average | O(log n) average |
| Validate BST | Medium | O(n) | O(h) |
| BST Traversal | Medium | O(n) | O(n) |
| Min Height BST | Medium | O(n) | O(n) |

### Dynamic Programming

Complex problems solved using optimal substructure and overlapping subproblems.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Max Subset Sum No Adjacent | Medium | O(n) | O(1) |
| Number of Ways to Make Change | Medium | O(nd) | O(n) |
| Levenshtein Distance | Medium | O(nm) | O(nm) |
| Min Number of Coins For Change | Medium | O(nd) | O(n) |
| Max Sum Increasing Subsequence | Hard | O(n²) | O(n) |
| Longest Common Subsequence | Hard | O(nm) | O(nm) |

#### Featured Solution: Levenshtein Distance

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

### Graphs

Network and traversal problems modeled using graph data structures.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Depth-First Search | Easy | O(V + E) | O(V) |
| Breadth-First Search | Medium | O(V + E) | O(V) |
| River Sizes | Medium | O(wh) | O(wh) |
| Youngest Common Ancestor | Medium | O(d) | O(1) |

### Greedy Algorithms

Solving optimization problems by making locally optimal choices at each stage.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Minimum Waiting Time | Easy | O(n log n) | O(1) |
| Class Photos | Easy | O(n log n) | O(1) |
| Tandem Bicycle | Easy | O(n log n) | O(1) |
| Task Assignment | Medium | O(n log n) | O(n) |

### Recursion

Implementing elegant solutions to problems that can be defined in terms of similar subproblems.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Nth Fibonacci | Easy | O(n) | O(1) |
| Product Sum | Easy | O(n) | O(d) |
| Permutations | Medium | O(n*n!) | O(n*n!) |
| Powerset | Medium | O(n*2ⁿ) | O(n*2ⁿ) |

### Stacks

Implementations leveraging Last-In-First-Out data structures.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Min Max Stack Construction | Medium | O(1) | O(n) |
| Balanced Brackets | Medium | O(n) | O(n) |
| Sunset Views | Medium | O(n) | O(n) |

### Strings

Text processing algorithms and string manipulation.

| Algorithm | Difficulty | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| Palindrome Check | Easy | O(n) | O(1) |
| Caesar Cipher Encryptor | Easy | O(n) | O(n) |
| Longest Palindromic Substring | Medium | O(n²) | O(n) |
| Group Anagrams | Medium | O(w * n * log n) | O(wn) |

## 🔄 Automated Testing

In 2024, I developed a Bash automation system to streamline testing of all implementations. The `run.sh` script:

1. **Executes all algorithm implementations** in `/Executionary Code` directories
2. **Captures output** from Python, JavaScript, and C# files
3. **Organizes results** in a mirrored folder structure in `/Test Outputs`
4. **Generates test reports** for easy verification of algorithm correctness

### Test Automation in Action

![run-demo](run.mp4)
*Automated test script execution*

The generated folder structure maintains perfect synchronization with the source code:

![run-pic](run.PNG)
*Generated test output directory structure*

## 🚀 Running the Code

### Prerequisites

- Python 3.x
- Node.js
- .NET SDK (for C# files)
- Bash shell environment

### Execution Steps

1. Clone this repository
2. Navigate to the repository root
3. Make the script executable:
   ```bash
   chmod +x run.sh
   ```
4. Execute the automation script:
   ```bash
   ./run.sh
   ```
5. Review test results in the `/Test Outputs` directory


---

*Developed by Joel Mattsson*