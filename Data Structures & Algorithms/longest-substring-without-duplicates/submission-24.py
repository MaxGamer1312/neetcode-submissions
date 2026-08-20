class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = {}
        i = 0
        longest_substring_len = 0
        for j in range(len(s)):
            if s[j] in bucket:
                i = max(bucket[s[j]]+1, i)
            bucket[s[j]] = j
            longest_substring_len = max(longest_substring_len, j - i + 1)
        return longest_substring_len