# python validating-starting-city.py

# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    amountOfCities = len(distances)
    distanceToDriveLeft = (fuel[0] * mpg) - distances[0]
    minDistance = distanceToDriveLeft
    startingCity = 1

    for i in range(1, amountOfCities):
        distanceToDriveLeft += (fuel[i] * mpg) - distances[i]

        if distanceToDriveLeft < minDistance:
            minDistance = distanceToDriveLeft
            startingCity = (i + 1) % amountOfCities

    return startingCity

def runTestCases():
    print("")
    print("")
    print("validating-starting-city.py:")

    print(validStartingCity([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10)) # Expected output: 4
    print(validStartingCity([15, 20, 25, 30, 35, 5], [0, 3, 0, 0, 1, 1], 26)) # Expected output: 5

runTestCases()