class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        for i, height in enumerate(heights):
            start_index = i
            while stack and height < stack[-1][0]:
                temp_info = stack.pop()
                temp_result = temp_info[0] * (i - temp_info[1])
                result = max(result, temp_result)
                start_index = temp_info[1]
            stack.append((height, start_index))
        while stack:
            temp_info = stack.pop()
            temp_result = temp_info[0] * (len(heights) - temp_info[1])
            result = max(result, temp_result)
        return result