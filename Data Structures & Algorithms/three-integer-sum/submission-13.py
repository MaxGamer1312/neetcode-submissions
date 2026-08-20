class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 1):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                if j != i+1 and nums[j-1] == nums[j]:
                    j += 1
                    continue
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return result