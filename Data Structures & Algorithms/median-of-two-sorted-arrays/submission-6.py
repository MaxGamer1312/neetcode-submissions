class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = (len(nums1) + len(nums2)) // 2
        if not nums1:
            if len(nums2) % 2 == 0:
                return (nums2[median] + nums2[median-1]) / 2
            return nums2[median]
        if not nums2:
            if len(nums1) % 2 == 0:
                return (nums1[median] + nums1[median-1]) / 2
            return nums1[median]
        i = 0
        j = len(nums1) - 1
        while i <= j:
            first_half_index = (i + j) // 2
            second_half_index = (median-1) - (first_half_index+1)
            if second_half_index >= 0 and second_half_index < len(nums2) and first_half_index+1 < len(nums1):
                if nums2[second_half_index] > nums1[first_half_index+1]:
                    i = first_half_index + 1
                    
                    continue
            if second_half_index+1 < len(nums2):
                if nums1[first_half_index] > nums2[second_half_index+1]:
                    j = first_half_index - 1
                    continue
            break

        if j == -1:
            first_half_index = -1
            second_half_index = (median-1)
        right_num = 0
        if first_half_index+1 < len(nums1):
            if second_half_index+1 < len(nums2):
                right_num = min(nums1[first_half_index+1], nums2[second_half_index+1])
            else:
                right_num = nums1[first_half_index+1] 
        else:
            right_num = nums2[second_half_index+1]
        if (len(nums1) + len(nums2)) % 2 == 0:
            if second_half_index != -1 and first_half_index != -1:
                left_num = max(nums1[first_half_index], nums2[second_half_index])
            elif first_half_index == -1:
                left_num = nums2[second_half_index]
            else:
                left_num = nums1[first_half_index]
            return (left_num + right_num) / 2
        else:
            return right_num
