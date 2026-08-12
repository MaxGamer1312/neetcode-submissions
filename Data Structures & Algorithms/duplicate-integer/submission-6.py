class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testMap = set()
        for i in nums:
            if(i in testMap):
                return True
            testMap.add(i)
        return False
            
         