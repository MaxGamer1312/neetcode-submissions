class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        left_max_height = height[i]
        right_max_height = height[j]
        total = 0
        while i < j:
            if left_max_height < right_max_height:
                total += min(left_max_height, right_max_height) - height[i]
                i += 1
                left_max_height = max(left_max_height, height[i])
            else:
                total += min(left_max_height, right_max_height) - height[j]
                j -= 1
                right_max_height = max(right_max_height, height[j])
        return total
