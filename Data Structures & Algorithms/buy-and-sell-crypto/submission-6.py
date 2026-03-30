class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):

            if r < len(prices) - 1 and prices[r] < prices[l]:
                l = r
            while r < len(prices)-1 and prices[r] < prices[r+1]:
                r += 1
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit





