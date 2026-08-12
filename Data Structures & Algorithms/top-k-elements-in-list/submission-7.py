class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            if num in result:
                result.sort(key=lambda x: count[x])
                continue
            if len(result) < k:
                self.binary_add(num, result, count)
            elif count[num] > count[result[0]]:
                result.pop(0)
                self.binary_add(num, result, count)
        return result
    
    def binary_add(self, element, result, count):
        i = 0
        j = len(result) - 1
        while i <= j:
            middle_index = (i + j) // 2
            middle_element = result[middle_index]
            if count[element] > count[middle_element]:
                i = middle_index + 1
            elif count[element] < count[middle_element]:
                j = middle_index - 1
            else:
                i = j + 1
        result.insert(i, element)