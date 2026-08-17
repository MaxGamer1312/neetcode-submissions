class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        result = nums[len(nums) - 1]
        while i <= j:
            middle_index = (i + j) // 2
            middle_element = nums[middle_index]
            if middle_element >= nums[j]:
                i = middle_index + 1
            else:
                j = middle_index - 1
            if middle_element < result:
                result = middle_element
        return result