let array = [1, 2, 3, 4]
const n = array.length

// powersetRecursive(array, n - 1)
// console.log(powersetRecursive(array, n - 1))

runTestCases()

// TODO: Add graphical visualization of my paper-sketches


// O(2^n * n/2) = O(2^n * n) time complexity
// O(2^n * n) space complexity

// Recursive logical formula: P([1, 2, 3]) = P([1, 2]) + [3], where [3] is combined individually with each element of P([1, 2])

// To achieve this in code, we continiously decrease the index and read the elements as
// we go further down in recursive frames, until we hit the base case. Once this case
// is hit, we first combine its subsets (starting from the minimal index so that
// we do it in the same sequential order as in the iterative approach). After the
// subsets are registered, we go back up in the callstack to perform the same
// action on the element with a greater index

function powersetRecursive(array, idx) {

    // Base case:
    if (idx < 0) {
        return [[]]
    }

    let currentElement = array[idx]
    let subsets = powersetRecursive(array, idx - 1)


    // Once the base case is hit, the code below is executed

    let currentSubsetsLength = subsets.length

    for (let i = 0; i < currentSubsetsLength; i++) {
        let currentSubsetElement = subsets[i]

        if (i == 0) {
            subsets.push([currentElement])
        } else {
            let newSubsetArr = currentSubsetElement.concat(currentElement)
            subsets.push(newSubsetArr)
        }
    }

    return subsets
}


function runTestCases() {
    let test1 = [1]
    const n1 = test1.length
    console.log(powersetRecursive(test1, n1 - 1)) // Expected output: 2^1 = 2 subsets

    console.log("")
    console.log("")

    let test2 = [1, 2]
    const n2 = test2.length
    console.log(powersetRecursive(test2, n2 - 1)) // Expected output: 2^2 = 4 subsets

    console.log("")
    console.log("")

    let test3 = [1, 2, 3]
    const n3 = test3.length
    console.log(powersetRecursive(test3, n3 - 1)) // Expected output: 2^3 = 8 subsets

    console.log("")
    console.log("")

    let test4 = [1, 2, 3, 4]
    const n4 = test4.length
    console.log(powersetRecursive(test4, n4 - 1)) // Expected output: 2^4 = 16 subsets

    console.log("")
    console.log("")

    let test5 = [1, 2, 3, 4, 5]
    const n5 = test5.length
    console.log(powersetRecursive(test5, n5 - 1)) // Expected output: 2^5 = 32 subsets
}