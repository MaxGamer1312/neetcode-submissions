class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        for height in heights:
            if not stack or height > stack[-1][0]:
                stack.append([height, 1])
            elif height == stack[-1][0]:
                stack[-1][1] += 1
            else:
                temp_info = [height, 1]
                while stack and height < stack[-1][0]:
                    prevArea = stack[-1][0] * (stack[-1][1] + temp_info[1] - 1)
                    if prevArea > result:
                        result = prevArea
                    prev_info = stack.pop()
                    temp_info[1] += prev_info[1]
                stack.append(temp_info)
        while stack:
            prevArea = stack[-1][1] * stack[-1][0]
            if prevArea > result:
                result = prevArea
            prev_info = stack.pop()
            if stack:
                stack[-1][1] += prev_info[1]
        return result
