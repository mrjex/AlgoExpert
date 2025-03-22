// Command: "node youngest-common-ancestor.js"

class Ancestor {
    constructor(name) {
        this.name = name
        this.ancestor = null
    }

    setAncestor(otherAncestor) {
        this.ancestor = otherAncestor
    }
}

runTestCase()
  
/*
    'topAncestor' always has depth 0 and points to null ancestor
*/
function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
    let depthOne = getDepth(topAncestor, descendantOne)
    let depthTwo = getDepth(topAncestor, descendantTwo)

    let depthDifference = Math.abs(depthOne - depthTwo)

    if (depthOne > depthTwo) {
    return traceYoungestAncestor(descendantOne, descendantTwo, depthDifference)
    }
    
    return traceYoungestAncestor(descendantTwo, descendantOne, depthDifference)
}

function getDepth(topAncestor, node) {
    let depth = 0;
    while (node != topAncestor) {
    node = node.ancestor;
    depth++;
    }

    return depth;
}

function traceYoungestAncestor(lowerDescendant, higherDescendant, difference) {

    // Stabilize height-levels of the two descendants
    while (difference > 0) {
        lowerDescendant = lowerDescendant.ancestor
        difference--
    }

    // Once both levels are equal, move both toward the top ancestor in parallel with each other
    while (lowerDescendant != higherDescendant) {
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    }

    return higherDescendant
}


function runTestCase() {

    // Create graph
    const topAncestor = new Ancestor("A")

    const b = new Ancestor("B")
    b.setAncestor(topAncestor)

    const c = new Ancestor("C")
    c.setAncestor(topAncestor)

    const d = new Ancestor("D")
    d.setAncestor(b)

    const e = new Ancestor("E")
    e.setAncestor(b)

    const f = new Ancestor("F")
    f.setAncestor(c)

    const g = new Ancestor("G")
    g.setAncestor(c)

    const h = new Ancestor("H")
    h.setAncestor(d)

    const i = new Ancestor("I")
    i.setAncestor(d)

    // Run test cases
    console.log(getYoungestCommonAncestor(topAncestor, e, i)); // Expected output: B
    console.log(getYoungestCommonAncestor(topAncestor, e, h)); // Expected output: B
    console.log(getYoungestCommonAncestor(topAncestor, h, e)); // Expected output: B

    console.log(getYoungestCommonAncestor(topAncestor, h, i)); // Expected output: D
    console.log(getYoungestCommonAncestor(topAncestor, d, i)); // Expected output: D

    console.log(getYoungestCommonAncestor(topAncestor, f, g)); // Expected output: C

    console.log(getYoungestCommonAncestor(topAncestor, h, c)); // Expected output: A
}
  