class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i <= j:
            width = j-i
            height = min(heights[i],heights[j])
            area = width * height
            print(heights[i])
            print(heights[j])
            print(area)
            print("#############")
            if area > maxArea:
                maxArea = area
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxArea