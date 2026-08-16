class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        result = 0
        stack = []
        for i in range(len_heights + 1):
            start_index = i
            while stack and (i == len_heights or heights[i] < stack[-1][0]):
                temp_info = stack.pop()
                temp_result = temp_info[0] * (i - temp_info[1])
                result = max(result, temp_result)
                start_index = temp_info[1]
            if i == len_heights:
                continue
            stack.append((heights[i], start_index))
        print(stack)
        return result