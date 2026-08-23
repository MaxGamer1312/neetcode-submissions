import bisect
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [-float("inf")] * (len(nums)-k+1)
        sorted_nums = []
        for i in range(0, k):
            bisect.insort(sorted_nums, (nums[i], i))
        for i in range(k-1, len(nums)):
            bisect.insort(sorted_nums, (nums[i], i))
            for j in range(len(sorted_nums)-1, -1, -1):
                if sorted_nums[j][1] >= i-k+1:
                    result[i-k+1] = sorted_nums[j][0]
                    break
        return result