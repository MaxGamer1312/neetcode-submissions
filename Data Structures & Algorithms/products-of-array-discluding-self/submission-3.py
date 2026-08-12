class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        target = 1
        zeroCount = 0
        for i in nums:
            if i == 0:
                zeroCount += 1
            if i != 0:
                target *= i
        if(zeroCount >= 2):
            return [0] * len(nums)
        elif(zeroCount == 1):
            for i in nums:
                if i != 0:
                    answer.append(0)
                else:
                    answer.append(int(target))
        else:
            for i in nums:
                answer.append(int(target/i))    
        return answer