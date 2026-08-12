class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        maxHeight = 0
        for i in height:
            prefix.append(maxHeight)
            if i > maxHeight:
                maxHeight = i
        maxHeight = 0
        for i in reversed(height):
            suffix.insert(0,maxHeight)
            if i > maxHeight:
                maxHeight = i
            
        answer = 0
        for i,element in enumerate(height):
            answer += max(0,min(prefix[i],suffix[i]) - element)
        return answer
                
