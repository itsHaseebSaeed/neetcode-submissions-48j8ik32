class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        i=0

        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[i] < prices[j]:
                profit = max(profit, prices[j]- prices[i])
                j+=1

            i = j

        return profit        