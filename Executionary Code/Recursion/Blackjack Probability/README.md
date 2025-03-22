# Blackjack Probability

Input:
 - target: 21
 - startingHand: 15

Busting / Losing: Going above the target value


Stopping point: 21 - 4 = 17


O(t-s) time complexity --> The number of recursive calls scales linearly with that value
O(t-s) space complexity (the memo scales the same way)


Create 'memo' dictionary to avoid recalculating values
