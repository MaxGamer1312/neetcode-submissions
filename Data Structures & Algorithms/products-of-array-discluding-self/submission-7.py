class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix = len_nums * [1]
        postfix = len_nums * [1]
        result = len_nums * [1]
        for i in range(len_nums):
            j = (len_nums - 1) - i
            if i > 0:
                prefix[i] *= prefix[i-1] * nums[i-1]
                result[i] *= prefix[i]
            if j < len_nums - 1:
                postfix[j] = postfix[j+1] * nums[j+1]
                result[j] *= postfix[j]
        return result