# t - Amount of tasks (2k)
# O(t^2 + 0.5t + nlog(n)) = O(t^2 + nlog(n)) = O((2k)^2 + nlog(n)) time | O(t) space
def taskAssignment(k, tasks):
    # tasks = [1, 3, 5, 3, 1, 4]
    sortedTasks = sorted(tasks)  # [1, 1, 3, 3, 4, 5]
    sortedTasksOriginalIndices = [-1 for _ in tasks]  # [-1, -1, -1, -1, -1, -1]

    for i in range(len(tasks)):
        for j in range(len(sortedTasks)):
            if tasks[i] == sortedTasks[j] and sortedTasksOriginalIndices[j] == -1:
                sortedTasksOriginalIndices[j] = i
                break

    left, right = 0, len(tasks) - 1
    optimalTaskAssignments = []
    while left < right:
        optimalTaskAssignments.append([sortedTasksOriginalIndices[left], sortedTasksOriginalIndices[right]])
        left += 1
        right -= 1
    return optimalTaskAssignments


def runTestCases():
    print("")
    print("")
    print("task-assignment.py:")

    print(taskAssignment(3, [1, 3, 5, 3, 1, 4])) # Expected output: [[0, 2], [4, 5], [1, 3]]
    print(taskAssignment(2, [3, 4, 5 ,3])) # Expected output: [[0, 2], [3, 1]]

runTestCases()