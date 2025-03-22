# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    minNumberOfCoins = [0] + [float("inf") for _ in range(n)]

    for denom in denoms:
        for c in range(len(minNumberOfCoins)):
            if denom <= c: # If the current denom is less than or equal coin we are trying to replace, it means that the denom fits inside the coin (as a term that can be added to make it a sum)
                minNumberOfCoins[c] = min(minNumberOfCoins[c], 1 + minNumberOfCoins[c - denom])
                
    return minNumberOfCoins[n] if minNumberOfCoins[n] != float("inf") else -1


def runTestCases():
    print("")
    print("")
    print("min-number-coins-change.py")

    print(minNumberOfCoinsForChange(7, [1, 5, 10])) # Expected output: 3 (1x1 + 1x1 + 1x5 <=> 2x1 + 1x5)
    print(minNumberOfCoinsForChange(5, [1, 5, 10])) # Expected output: 1 (1x5)
    print(minNumberOfCoinsForChange(4, [1, 5, 10])) # Expected output: 4 (4x1)
    print(minNumberOfCoinsForChange(100, [1, 5, 10])) # Expected output: 10 (10x10)
    print(minNumberOfCoinsForChange(99, [1, 5, 10])) # Expected output: 14 (9x10 + 1x5 + 4x1)
    print(minNumberOfCoinsForChange(40, [1, 2, 20])) # Expected output: 2 (2x20)
    print(minNumberOfCoinsForChange(45, [1, 2, 20])) # Expected output: 5 (2x20 + 2x2 + 1x1)

runTestCases()