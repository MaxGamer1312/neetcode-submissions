class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxNum = 0
        while i < j:
            width = j - i
            if heights[i] < heights[j]:
                current_result = heights[i] * width
                i += 1
            else:
                current_result = heights[j] * width
                j -= 1
            if maxNum < current_result:
                maxNum = current_result
        return maxNum