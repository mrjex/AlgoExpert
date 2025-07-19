# AlgoExpert

> A collection of Algorithm & Data structure implementations during the summer of 2022

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![C#](https://img.shields.io/badge/C%23-.NET-purple)](https://dotnet.microsoft.com/languages/csharp)
[![Bash](https://img.shields.io/badge/Bash-Script-green)](https://www.gnu.org/software/bash/)
[![AlgoExpert](https://img.shields.io/badge/Practice-AlgoExpert-orange)](https://www.algoexpert.io/)

## Table of Contents

- [AlgoExpert](#algoexpert)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Repository Structure](#repository-structure)
  - [Running the Code](#running-the-code)
  - [Automated Testing](#automated-testing)
    - [Test Automation in Action](#test-automation-in-action)

## Overview

This repository documents my algorithmic journey, showcasing implementations of various data structures and algorithms. Initially developed in Summer 2022 to refine my problem-solving skills in Python, this collection has grown to include multiple data structures across further programming languages.


## Repository Structure

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


## Running the Code

**Prerequisites:** *Python 3.x*, *Node.js*, *.NET SDK* and *Bash/Shell environment*

1. Clone repository
2. Navigate to root directory
3. Make script executable:
   ```bash
   chmod +x run.sh
   ```
4. Execute automation script:
   ```bash
   ./run.sh
   ```
5. Review test results in `/Test Outputs`



## Automated Testing

In 2024, I developed a Bash automation system to streamline testing of all implementations. The `run.sh` script:

1. **Executes all algorithm implementations** in `/Executionary Code` directories
2. **Captures output** from Python, JavaScript, and C# files
3. **Organizes results** in a mirrored folder structure in `/Test Outputs`
4. **Generates test reports** for easy verification of algorithm correctness

### Test Automation in Action

[![AlgoExpert Testing Framework - Demo](https://img.youtube.com/vi/TenIHvCpTzM/maxresdefault.jpg)](https://www.youtube.com/watch?v=TenIHvCpTzM)

*Automated test script execution*

The generated folder structure maintains perfect synchronization with the source code:

![run-pic](run.PNG)

*Generated test output directory structure*
