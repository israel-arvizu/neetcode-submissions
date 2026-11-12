class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowPointer, highPointer = 0, 1
        highestProfit = 0

        while highPointer != len(prices):
            lowPointerPrice = prices[lowPointer]
            highPointerPrice = prices[highPointer]

            if lowPointerPrice < highPointerPrice:
                profit = highPointerPrice - lowPointerPrice
                highestProfit = max(highestProfit, profit)
            else:
                lowPointer = highPointer

            highPointer += 1

        return highestProfit