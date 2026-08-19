class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        len_num1 = len(nums1)
        if len_num1 % 2 != 0:
            return nums1[(len_num1 - 1)//2]
        return (nums1[(len_num1 - 1)//2] + nums1[(len_num1 - 1)//2+1]) / 2