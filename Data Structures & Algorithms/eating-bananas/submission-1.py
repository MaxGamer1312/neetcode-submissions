class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        minK = j
        while i <= j:
            curr_h = 0
            mid = i + ((j - i) // 2)
            for bananas in piles:
                curr_h += int(math.ceil(bananas / mid))
            print(mid)
            print(curr_h)
            print(i)
            print(j)
            print("#############")
            if curr_h > h:
                i = mid + 1
            elif curr_h <= h:
                if mid < minK:
                    minK = mid
                j = mid - 1

        return minK