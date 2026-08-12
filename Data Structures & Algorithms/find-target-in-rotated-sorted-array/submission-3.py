class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + ((j - i) // 2)
            if nums[mid] == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            elif nums[i] < nums[mid] and target > nums[i] and target < nums[mid]:
                j = mid - 1
            elif nums[mid] < nums[j] and target > nums[mid] and target < nums[j]:
                i = mid + 1
            elif nums[i] > nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1

        