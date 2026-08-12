class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        result = []
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            self.binary_add(num, result, counts)
            if len(result) > k:
                result.pop(len(result) - 1)
        return result

    def binary_add(self, element, result, counts):
        i = 0
        j = len(result)
        while i < j:
            middle_index = (i + j) // 2
            if counts[element] > counts[result[middle_index]]:
                j = middle_index
            else:
                i = middle_index + 1
        result.insert(i, element)