class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            mid = int(i / 2 + j / 2)
            if nums[mid] == target:
                return mid
            elif mid != i and nums[mid] < target:

                i = mid
            else:
                if mid == j:
                    return -1
                j = mid
        return -1