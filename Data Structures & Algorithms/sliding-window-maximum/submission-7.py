import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [-float("inf")] * (len(nums)-k+1)
        max_heap = []
        for i in range(0, k):
            heapq.heappush_max(max_heap, (nums[i], i))
        for i in range(k-1, len(nums)):
            heapq.heappush_max(max_heap, (nums[i], i))
            while max_heap and max_heap[0][1] < i-k+1:
                heapq.heappop_max(max_heap)
            result[i-k+1] = max_heap[0][0]
        return result