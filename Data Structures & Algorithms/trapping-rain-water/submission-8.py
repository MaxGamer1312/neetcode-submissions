class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        i = 0
        j = len(height) - 1
        current_highest_level = 0
        while i < j:
            min_height = min(height[i], height[j])
            current_area = min_height * (j - i - 1)
            prev_area = current_highest_level * (j - i - 1)
            if min_height > current_highest_level:
                total_water += current_area - prev_area
                current_highest_level = min_height
            if height[i] < height[j]:
                i += 1
                if i != j:
                    total_water -= min(current_highest_level, height[i])
            else:
                j -= 1
                if j != i:
                    total_water -= min(current_highest_level, height[j])
        return total_water
            
