class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = {}
        result = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited[nums[i]] = i
            for j in range(len(nums)):
                if i == j:
                    continue
                n3 = -(nums[i] + nums[j])
                current_result = tuple(sorted([nums[i], nums[j], n3]))
                if n3 in visited and current_result not in result and visited[n3] != i and visited[n3] != j:
                    result.add(current_result)
        return list(result)