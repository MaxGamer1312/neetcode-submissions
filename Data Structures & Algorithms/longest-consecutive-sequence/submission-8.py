class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        test = set()
        for i in nums:
            test.add(i)
        maxCount = 0
        currCount = 0
        for i,element in enumerate(nums):
            if nums[i] - 1 in test:
                continue
            add = 0
            while element + add in test:
                print(element + add)
                currCount += 1
                add += 1
                
            if currCount > maxCount:
                maxCount = currCount
            currCount = 0
            
        return maxCount