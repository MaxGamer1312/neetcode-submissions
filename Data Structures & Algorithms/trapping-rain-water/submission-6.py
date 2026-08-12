class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        maxHeight = 0
        for i in height:
            
            if i > maxHeight:
                maxHeight = i
            prefix.append(maxHeight)
        maxHeight = 0
        for i in reversed(height):
            if i > maxHeight:
                maxHeight = i
            suffix.insert(0,maxHeight)
            
        answer = 0
        for i,element in enumerate(height):
            answer += min(prefix[i],suffix[i]) - element
        return answer
                
