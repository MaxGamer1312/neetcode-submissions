class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        check = {}
        for i,elem in enumerate(nums):
            check[elem] = i
        dupe = set()
        answers = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                answer = nums[i] + nums[j]
                answer = -answer
                temp = (nums[i], nums[j], answer)
                temp = sorted(temp)
                temp = tuple(temp)
                print(temp)
                if temp in dupe:
                    continue
                if answer in check and check[answer] != i and check[answer] != j:
                    answers.append([nums[i], nums[j], answer])
                    dupe.add(temp)
        return answers
