class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + ((j - i) // 2)
            print(nums[i])
            print(nums[j])
            print(nums[mid])
            if nums[mid] == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            elif nums[i] < nums[mid] and target > nums[i] and target < nums[mid]:
                print("#")
                j = mid - 1
            elif nums[mid] < nums[j] and target > nums[mid] and target < nums[j]:
                print("##")
                i = mid + 1
            elif nums[i] > nums[mid]:
                print("###")
                j = mid - 1
            else:
                print("####")
                i = mid + 1
        return -1

        