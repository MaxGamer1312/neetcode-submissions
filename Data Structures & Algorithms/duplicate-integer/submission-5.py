class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testMap = set()
        test = True
        for i in nums:
            if(i in testMap):
                return True
            testMap.add(i)
        if(test):
            return False
            
         