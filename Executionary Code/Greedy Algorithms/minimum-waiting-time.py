# python minimum.waiting-time.py


# O(n * logn(n) + n) = O(n * log(n)) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()  # O(n * logn(n)) time
    minWaitingTime = 0
    currentTime = queries[0]

    for i in range(1, len(queries)):  # O(n) time
        minWaitingTime += currentTime
        currentTime += queries[i]
    return minWaitingTime


def runTestCases():
    print("")
    print("")
    print("minimum.waiting-time.py")

    print(minimumWaitingTime([3, 2, 1, 2, 6])) # Expected output: 17
    print(minimumWaitingTime([2, 1, 1, 1])) # Expected output: 6
    print(minimumWaitingTime([25, 30, 2, 1])) # Expected output: 32

runTestCases()