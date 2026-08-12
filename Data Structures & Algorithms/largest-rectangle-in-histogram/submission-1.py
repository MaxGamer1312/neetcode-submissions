class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append([0,0])
        maxArea = 0
        for i,value in enumerate(heights):
            lastIndex = i
            while len(stack) != 0 and value < stack[-1][0]:
                currArea = stack[-1][0] * (i-stack[-1][1])
                lastIndex = stack[-1][1]
                print(stack)
                print((i-stack[-1][1]))
                if maxArea < currArea:
                    maxArea = currArea
                stack.pop()
            stack.append([value,lastIndex])
        for value,i in stack:
            maxArea = max(maxArea, value * (len(heights) - i))
        return maxArea