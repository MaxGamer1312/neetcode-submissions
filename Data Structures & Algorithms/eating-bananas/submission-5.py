class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low_k = 1
        high_k = max(piles)
        while low_k <= high_k:
            middle_k = (low_k + high_k) // 2
            total_hours = self.getTime(piles, middle_k)
            if total_hours <= h:
                high_k = middle_k - 1
            elif total_hours > h:
                low_k = middle_k + 1
        return low_k

    def getTime(self, piles, k):
        total_hours = 0
        for pile in piles:
            total_hours += -(pile//-k)
        return total_hours
