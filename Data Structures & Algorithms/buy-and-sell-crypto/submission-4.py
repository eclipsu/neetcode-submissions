class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            sell = prices[r] - prices[l]
            profit = max(profit, sell)

            if prices[r] < prices[l]:
                l = r
            r += 1
        return profit
