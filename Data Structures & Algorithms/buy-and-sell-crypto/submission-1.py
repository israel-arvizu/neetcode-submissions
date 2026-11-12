class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0 

        # go through the items in the list
        for i in range(len(prices)):
            # comapre the profit of the minimum bs the current index
            if (prices[i] - minPrice) > maxProfit:
                # if its profitable, udpate the max profit
                maxProfit = prices[i] - minPrice
            else:
                if prices[i] < minPrice:
                    minPrice = min(minPrice, prices[i])

        return maxProfit
        