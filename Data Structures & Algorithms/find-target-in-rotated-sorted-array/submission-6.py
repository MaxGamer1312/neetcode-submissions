class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            middle_index = (i+j) // 2
            middle_element = nums[middle_index]
            if target == middle_element:
                return middle_index
            if target == nums[i]:
                return i
            if target == nums[j]:
                return j
            if nums[i] <= middle_element:
                if target < middle_element and target > nums[i]:
                    j = middle_index - 1
                else:
                    i = middle_index + 1
            elif middle_element < nums[j]:
                if target >= middle_element and target <= nums[j]:
                    i = middle_index + 1
                else:
                    j = middle_index - 1
        return -1