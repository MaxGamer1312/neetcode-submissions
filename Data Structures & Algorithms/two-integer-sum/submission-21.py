class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        test = {}
        for j in range(len(nums)):
            result = target - nums[j]
            test[result] = j
        for i in range(len(nums)):
            if(nums[i] in test and i != test[nums[i]]):
                answer = []
                answer.append(i)
                answer.append(test[nums[i]])
                return answer
            
        