# O(m + n + c) time | O(c) space
def generateDocument(characters, document):
    lettersInDocument = {}
    
    # O(m)
    for i in range(len(document)):
        currentLetter = document[i]

        if currentLetter not in lettersInDocument:
            lettersInDocument[currentLetter] = 1
        else:
            lettersInDocument[currentLetter] += 1
    
    # O(n)
    for i in range(len(characters)):
        currentLetter = characters[i]

        if currentLetter in lettersInDocument:
            lettersInDocument[currentLetter] -= 1

    # O(c) - c represents the amount of unique characters in 'document'
    for key in lettersInDocument:
        if lettersInDocument[key] > 0:
            return False
    return True


def runTestcases():
    print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!")) # Expected output: True
    print(generateDocument("A", "a")) # Expected output: False
    print(generateDocument("a hsgalhsa sanbjksbdkjba kjx", "")) # Expected output: True
    print(generateDocument("estssa", "testing")) # Expected output: False


runTestcases()