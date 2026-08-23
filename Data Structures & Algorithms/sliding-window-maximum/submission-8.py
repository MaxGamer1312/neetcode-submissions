from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque([])
        for i in range(0, k-1):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
        for i in range(k-1, len(nums)):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
            result.append(dq[0])
            if dq and dq[0] == nums[i-k+1]:
                dq.popleft()
        return result