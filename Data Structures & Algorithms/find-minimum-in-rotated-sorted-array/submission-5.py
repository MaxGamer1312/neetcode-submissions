class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        minNum = nums[0]
        while i <= j:
            mid = i + ((j - i) // 2)
            print(nums[mid])
            if nums[mid] < minNum:
                minNum = nums[mid]
            if nums[mid] > nums[j] or nums[i] > nums[mid]:
                if nums[mid] > nums[j]:
                    i = mid + 1
                elif nums[i] > nums[mid]:
                    j = mid - 1
            else:
                return min(nums[i],minNum)
        return minNum
        