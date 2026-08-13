class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i = 0
        j = len(height) - 1
        max_left = height[i]
        max_right = height[j]
        total_water = 0
        while i < j:
            if height[i] < height[j]:
                i += 1
                max_left = max(max_left, height[i])
                min_index = i
            else:
                j -= 1
                max_right = max(max_right, height[j])
                min_index = j
            if i != j:
                total_water += max(0, min(max_left, max_right) - height[min_index])
        return total_water