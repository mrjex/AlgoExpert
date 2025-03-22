# O(w * n * log(n)) time | O(wn) space
def groupAnagrams(words):
    anagrams = {}
    for word in words:  # O(w)
        sortedWord = "".join(sorted(word))  # O(nlog(n))

        if sortedWord not in anagrams:
            anagrams[sortedWord] = [word]
        else:
            anagrams[sortedWord].append(word)

    return list(anagrams.values())  # O(w)


def runTestCases():

    # Expected output:
    # [["yo", "oy"], ["act", "tac", "cat"], ["flop", "olfp"], ["foo"]]
    print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))

    # Expected output:
    # [["zxc", "xcz"], ["asd", "sda"], ["weq", "qwe"]]
    print(groupAnagrams(["zxc", "asd", "weq", "sda", "qwe", "xcz"]))

    # Expected output:
    # ["yyo", "yo"]
    print(groupAnagrams(["yyo", "yo"]))


runTestCases()