class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_cost = float("-inf")
        for i in range(len(prices) - 1, -1 , -1):
            profit = max_cost - prices[i]
            if max_profit < profit:
                max_profit = profit
            if prices[i] > max_cost:
                max_cost = prices[i]
        return max_profit