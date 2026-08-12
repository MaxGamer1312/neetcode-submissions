class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for num in set_nums:
            if (num-1) in set_nums:
                continue
            curr_count = 1
            next_num = num + 1
            while next_num in set_nums:
                curr_count += 1
                next_num += 1
            if curr_count > max_count:
                max_count = curr_count
        return max_count