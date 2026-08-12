class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, element in enumerate(nums):
            current_target = target - element
            if current_target in visited:
                result = [i, visited[current_target]] if visited[current_target] > i else [visited[current_target], i]
                return result
            visited[element] = i