function blackjackProbability(target, startingHand) {
    let memo = {}
    let bustProbability = calculateBustProbability(target, startingHand, memo)
    return bustProbability
}

/*
    Calculates the probability for a card to reach 'Busted' state from the startingHand
*/
function calculateBustProbability(target, currentHand, memo) {
    if (memo[currentHand]) { // Use already calculated values in dictionary to avoid recalculation
        return memo[currentHand]
    }

    if (currentHand > target) { // Enter the state of busting
        return 1
    }

    if (currentHand >= target - 4) { // Enter the state of 'Standing', where no more cards are drawn. In other words, a 0% chance of busting
        return 0
    }

    // Recursively calculate the probability:

    let totalProbability = 0
    for (let drawnCard = 1; drawnCard <= 10; drawnCard++) { // Check possibilities for all 10 distinct cards in Blackjack
        const newCard = currentHand + drawnCard
        totalProbability += 0.1 * calculateBustProbability(target, newCard, memo)
    }

    memo[currentHand] = totalProbability
    return roundWithDecimalPlaces(totalProbability, 3)
}

function roundWithDecimalPlaces(num, n) { // 'n' is the number of decimal places
    return Math.round(num * Math.pow(10, n)) / Math.pow(10, n)
}

function runTestCases() {
    console.log(blackjackProbability(21, 13)) // Expected output: 0.335
    console.log(blackjackProbability(21, 15)) // Expected output: 0.45
    console.log(blackjackProbability(100, 20)) // Expected output: 0.273
}

runTestCases()