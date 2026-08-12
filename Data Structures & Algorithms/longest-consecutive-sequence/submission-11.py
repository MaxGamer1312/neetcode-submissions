class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for num in set_nums:
            if (num-1) in set_nums:
                continue
            length = 1
            while num + length in set_nums:
                length += 1
            if length > max_count:
                max_count = length
        return max_count