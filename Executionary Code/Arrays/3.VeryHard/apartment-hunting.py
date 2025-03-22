# Below, 2 solutions of the same problem are presented, one of which is more inefficient
# with O(b^2 * r) time, and one that is more elegant with O(br) time.


# Solution 1:

# O(b * r * b) = O(b^2 * r) time | O(2b * r) = O(br) space
def apartmentHuntingBruteForce(blocks, reqs):
    totalDistances = [0 for _ in blocks]
    furthestDistances = [float("-inf") for _ in blocks]

    for i in range(len(blocks)):
        minRequirementDistances = [float("inf")] * len(reqs)

        for r in range(len(reqs)):
            if blocks[i][reqs[r]]:
                minRequirementDistances[r] = 0
            else:
                for j in range(len(blocks)):
                    if j == i:
                        continue
                    if blocks[j][reqs[r]]:
                        minRequirementDistances[r] = min(minRequirementDistances[r], abs(i - j))

            totalDistances[i] += minRequirementDistances[r]
            furthestDistances[i] = max(furthestDistances[i], minRequirementDistances[r])

    return getOptimalBlock(blocks, furthestDistances)


def getOptimalBlock(blocks, furthestDistances):
    minDistance = float("inf")
    optimalBlockIdx = 0
    for x in range(len(blocks)):
        if furthestDistances[x] < minDistance:
            optimalBlockIdx = x
            minDistance = furthestDistances[x]

    return optimalBlockIdx


# Solution 2:

# O(r * 2b + br + b) = O(br) time | O(r* 2b + rb + b) = O(br)
def apartmentHuntingElegant(blocks, reqs):
    minDistancesFromBlocks = getRequirementDistancesFromBlocks(blocks, reqs, [[None] for a in reqs])
    furthestRequirements = getFurthestRequirementsInBlocks(blocks, reqs, minDistancesFromBlocks, [float("-inf") for a in blocks])
    return getOptimalBlockIndex(furthestRequirements)   

def getRequirementDistancesFromBlocks(blocks, reqs, outArr):
    for r in range(len(reqs)):
        closestReqIdx = float("inf")
        minDistances = [float("inf") for a in blocks]

        # Right to left
        for i in reversed(range(len(blocks))):
            if blocks[i][reqs[r]]:
                closestReqIdx = i
            minDistances[i] = abs(i - closestReqIdx)

        # Left to right
        for i in range(len(blocks)):
            if blocks[i][reqs[r]]:
                closestReqIdx = i
            minDistances[i] = min(abs(i - closestReqIdx), minDistances[i])
        outArr[r] = minDistances
    return outArr


def getFurthestRequirementsInBlocks(blocks, reqs, minDistancesFromBlocks, outArr):
    for b in range(len(blocks)):
        for r in range(len(reqs)):
            outArr[b] = max(outArr[b], minDistancesFromBlocks[r][b])
    return outArr


def getOptimalBlockIndex(furthestRequirements):
    minValue = furthestRequirements[0]
    minIdx = 0

    for i in range(1, len(furthestRequirements)):
        if furthestRequirements[i] < minValue:
            minIdx = i
            minValue = furthestRequirements[i]
    return minIdx


def runTestCases():
    print("")
    print("")
    print("apartment-hunting.py:")

    print(apartmentHuntingBruteForce([
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": True,
      "school": False,
      "store": False
    },
    {
      "gym": True,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": True
    }], ["gym", "school", "store"])) # Expected output: 3
  

    print(apartmentHuntingElegant([
        {
        "gym": True,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": True
        },
        {
        "gym": True,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": True,
        "store": False
        }], ["gym", "school", "store"])) # Expected output: 2


    print(apartmentHuntingElegant([
        {
        "gym": True,
        "office": False,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": True,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": True,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": True
        },
        {
        "gym": True,
        "office": True,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": True,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": True,
        "school": False,
        "store": False
        }
    ], ["gym", "pool", "school", "store"])) # Expected output: 4


runTestCases()