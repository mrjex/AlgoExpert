# O(n) time | O(n) space
def runLengthEncoding(string):
    encodedCharacters = []
    currentLength = 1

    for i in range(1, len(string)):
        currentChar = string[i]
        previousChar = string[i - 1]

        if currentChar != previousChar or currentLength == 9:
            appendDataToArray(encodedCharacters, [str(currentLength), previousChar])
            currentLength = 0

        currentLength += 1

    appendDataToArray(encodedCharacters, [str(currentLength), string[len(string) - 1]])
    return "".join(encodedCharacters)


def appendDataToArray(array, dataInArray):
    array.append(dataInArray[0])
    array.append(dataInArray[1])


def runTestcases():
    print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")) # Expected output: "9A4A2B4C2D"
    print(runLengthEncoding("122333")) # Expected output: "112233"
    print(runLengthEncoding("1A2BB3CCC4DDDD")) # Expected output: "111A122B133C144D"
    print(runLengthEncoding("[(aaaaaaa,bbbbbbb,ccccc,dddddd)]")) # Expected output: "1[1(7a1,7b1,5c1,6d1)1]"


runTestcases()