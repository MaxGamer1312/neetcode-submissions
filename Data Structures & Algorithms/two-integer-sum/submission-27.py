class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for i, element in enumerate(nums):
            self.binary_add([element, i], index_list)
        i = 0
        j = len(index_list) - 1
        while i != j:
            total = index_list[i][0] + index_list[j][0]
            if total == target:
                if index_list[i][1] < index_list[j][1]:
                    return [index_list[i][1], index_list[j][1]]
                return [index_list[j][1], index_list[i][1]]
            if total > target:
                j -= 1
            else:
                i += 1

    def binary_add(self, element, target_list):
        i = 0
        j = len(target_list) - 1
        while i <= j:
            middle_index = (i + j) // 2
            middle_element = target_list[middle_index][0]
            if element[0] > middle_element:
                i = middle_index + 1
            elif element[0] < middle_element:
                j = middle_index - 1
            else:
                i = j + 1
        target_list.insert(i, element)
