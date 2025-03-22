# Brute force solution:
# O(n^2) time | O(n) space
def minRewardsBruteForce(scores):
    outArr = [1] * len(scores)

    for i in range(1, len(scores) - 1):
        j = i - 1

        if scores[i] > scores[j]:
            outArr[i] = outArr[j] + 1
        else:
            while j >= 0 and scores[j] > scores[i]:
                outArr[j] += 1
                j -= 1

    return sum(outArr)


# Elegant solution (with resepct to the algortihm's complexity)
# O(n) time | O(n) space
def minRewardsElegant(array):
    if len(array) == 1:
        return 1
    
    localMinsIdx = []
    outArr = [1] * len(array)

    for i in range(len(array)):
        if i == 0:
            if array[1] > array[0]:
                localMinsIdx.append(0)

        elif i == len(array) - 1:
            if array[i - 1] > array[i]:
                localMinsIdx.append(i)

        elif array[i] < array[i - 1] and array[i] < array[i + 1]:
            localMinsIdx.append(i)

    for currentLocalMinIdx in localMinsIdx:
        leftIdx = currentLocalMinIdx - 1
        rightIdx = currentLocalMinIdx + 1

        counter = 2
        while leftIdx >= 0 and array[leftIdx] > array[leftIdx + 1]:
            outArr[leftIdx] = max(outArr[leftIdx], counter)

            leftIdx -= 1
            counter += 1

        counter = 2
        while rightIdx < len(array) and array[rightIdx - 1] < array[rightIdx]:
            outArr[rightIdx] = counter

            rightIdx += 1
            counter += 1

    return sum(outArr)


def runTestCases():
    print(minRewardsBruteForce([8, 4, 2, 1, 3, 6, 7, 9, 5])) # Expected output: 25
    print(minRewardsElegant([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0])) # Expected output: 52
    print(minRewardsElegant([800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53])) # Expected output: 93


runTestCases()