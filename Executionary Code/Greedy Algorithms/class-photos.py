# n - number of students in 1 team (red or blue)
# O(2 * (n * log(n)) + n) time = O(n * log(n)) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    mutualLength = len(redShirtHeights)
    redIsTaller = redShirtHeights[0] > blueShirtHeights[0]

    for i in range(mutualLength):
        if redShirtHeights[i] == blueShirtHeights[i]:
            return False
        elif (redShirtHeights[i] > blueShirtHeights[i]) != redIsTaller:
            return False
    return True

def runTestCases():
    print("")
    print("")
    print("class-photos.py")

    print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5])) # Expected output: True
    print(classPhotos([126], [125])) # Expected output: True
    print(classPhotos([1, 1, 1, 1, 1, 1, 1, 1], [5, 6, 7, 2, 3, 1, 2, 3])) # Expected output: False
    print(classPhotos([3, 5, 6, 8, 2, 1], [2, 4, 7, 5, 1, 6])) # Expected output: False

runTestCases()
