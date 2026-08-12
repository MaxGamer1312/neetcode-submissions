class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = len(nums) * [1]
        prefix_right = len(nums) * [1]
        result = []
        for i in range(len(nums)):
            j = (len(nums) - 1) - i
            if i > 0:
                prefix_left[i] = prefix_left[i-1] * nums[i-1]
            if j < len(nums) - 1:
                prefix_right[j] = prefix_right[j+1] * nums[j+1]
        for left_elem, right_elem in zip(prefix_left, prefix_right):
            result.append(left_elem * right_elem)
        return result