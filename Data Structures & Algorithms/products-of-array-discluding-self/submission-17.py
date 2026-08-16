class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        result = [1]
        for i in range(1, len_nums):
            result.append(nums[i-1] * result[i-1])
        postfix_num = 1
        for j in range(len_nums - 1, -1, -1):
            result[j] *= postfix_num
            postfix_num *= nums[j]
        return result