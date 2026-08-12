class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = prices[0]
        for Iright in range(1,len(prices)):
            right = prices[Iright]
            sellValue = right - left
            if right < left:
                left = right
            elif maxProfit < sellValue:
                maxProfit = sellValue
        return maxProfit