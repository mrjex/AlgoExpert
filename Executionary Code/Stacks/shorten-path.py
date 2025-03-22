# O(n) time, O(n) space
def shortenPath(path):
    isAbsolutePath = path[0] == "/"
    newPath = str.split(path, "/")
    filteredPath = []

    for i in range(len(newPath)):
        if newPath[i] != "." and newPath[i] != "":
            filteredPath.append(newPath[i])

    shortenedPath = []
    if isAbsolutePath:
        shortenedPath.append("")

    for i in range(len(filteredPath)):
        if filteredPath[i] == "..":
            if len(shortenedPath) == 0 or shortenedPath[-1] == "..":
                shortenedPath.append(filteredPath[i])
            elif shortenedPath[-1] != "":
                shortenedPath.pop()
        else:
            shortenedPath.append(filteredPath[i])

    return "/" if isAbsolutePath and len(shortenedPath) == 1 else "/".join(shortenedPath)

def runTestCases():
    print("")
    print("")
    print("shorten-path.py:")

    print(shortenPath("/foo/../test/../test/../foo//bar/./baz")) # Expected output: /foo/bar/baz
    print(shortenPath("../../foo/../../bar/baz")) # Expected output: ../../../bar/baz
    print(shortenPath("../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../..")) # Expected output: ../../../../../../../..
    print(shortenPath("./foo/bar")) # Expected output: foo/bar

runTestCases()