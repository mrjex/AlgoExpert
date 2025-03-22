let array = [1, 2, 3]
let outputTest = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

powerset(array)


// O(2^n * n/2) = O(2^n * n) time complexity
// O(2^n * n) space complexity

function powerset(array) {
    const n = array.length
    let subsets = [[]]

    for (let i = 0; i < n; i++) {
        let currentSubsetsLength = subsets.length
        let currentElement = array[i]

        // Iterate through all currently existing subsets and generate new combinations with the current element
        for (let j = 0; j < currentSubsetsLength; j++) {
            let currentSubsetElement = subsets[j]

            if (j == 0) {
                subsets.push([currentElement])
            } else {
                let newSubsetArr = currentSubsetElement.concat(currentElement)
                subsets.push(newSubsetArr)
            }
        }
    }

    console.log(subsets)
}