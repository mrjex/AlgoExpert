# O(1 time) | O(1) space
def validIPAddresses(string):
    foundValidIPAdresses = []
    inputLength = len(string)

    for i in range(1, min(inputLength, 4)):  # Max 3 times
        currentIPAdressParts = ["", "", "", ""]
        currentIPAdressParts[0] = string[:i]

        if not isValidPart(currentIPAdressParts[0]):
            continue

        for j in range(i + 1, min(inputLength, i + 4)):  # Max 3 times
            currentIPAdressParts[1] = string[i:j]
            if not isValidPart(currentIPAdressParts[1]):
                continue

            for k in range(j + 1, min(inputLength, j + 4)):  # Max 3 times
                currentIPAdressParts[2] = string[j:k]
                currentIPAdressParts[3] = string[k:]

                if isValidPart(currentIPAdressParts[2]) and isValidPart(currentIPAdressParts[3]):
                    foundValidIPAdresses.append(".".join(currentIPAdressParts))

    return foundValidIPAdresses

def isValidPart(string):  # O(1) time
    nr = int(string)
    if nr > 255:
        return False
    return str(nr) == string

def runTestCases():
    # Expected Output: ["1.9.216.80", "1.92.16.80", "1.92.168.0", "19.2.16.80", "19.2.168.0", "19.21.6.80", "19.21.68.0", "19.216.8.0", "192.1.6.80", "192.1.68.0", "192.16.8.0"]
    print(validIPAddresses("1921680"))

    # Expected Output: []
    print(validIPAddresses("255255255256"))

    # Expected Output: ["10.7.23.10", "10.7.231.0", "10.72.3.10", "10.72.31.0", "107.2.3.10", "107.2.31.0", "107.23.1.0"]
    print(validIPAddresses("1072310"))

runTestCases()