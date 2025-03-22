# n - The sum of elements in red- and blueShirtSpeeds
# O(n * log(n) + n) = O(n * log(n)) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    totalSpeedOfAllBicycles = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeedOfAllBicycles += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeedOfAllBicycles

def runTestCases():
    print("")
    print("")
    print("tandem-bicycle.py:")

    print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True)) # Expected output: 32
    print(tandemBicycle([3, 6, 7, 2, 1], [5, 5, 3, 9, 2], False)) # Expected output: 25
    print(tandemBicycle([1, 2, 1, 9, 12, 3], [3, 3, 4, 6, 1, 2], True)) # Expected output: 37

runTestCases()