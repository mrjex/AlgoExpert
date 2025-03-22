# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    output = []
    key %= 26

    for i, currentLetter in enumerate(string):
        output.append(getNewLetter(currentLetter, key))

    return "".join(output)

def getNewLetter(letter, key):
    temporaryCode = ord(letter) + key
    return chr((temporaryCode % 122) + 96) if temporaryCode > 122 else chr(temporaryCode)

def runTestcases():
    print(caesarCipherEncryptor("xyz", 2)) # Expected output: "zab"
    print(caesarCipherEncryptor("abc", 52)) # Expected output: "abc"
    print(caesarCipherEncryptor("iwufqnkqkqoolxzzlzihqfm", 25)) # Expected output: "hvtepmjpjpnnkwyykyhgpel"
    print(caesarCipherEncryptor("xyz", 5)) # Expected output: "cde"

runTestcases()