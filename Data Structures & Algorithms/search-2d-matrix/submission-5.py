class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix)
        while i < j-1:
            middle_index = (i + j) // 2
            middle_value = matrix[middle_index][0]
            if middle_value < target:
                i = middle_index
            elif middle_value > target:
                j = middle_index
            else:
                return True
        target_index = i
        i = 0
        j = len(matrix[0])
        while i < j-1:
            middle_index = (i + j) // 2
            middle_value = matrix[target_index][middle_index]
            if middle_value < target:
                i = middle_index
            elif middle_value > target:
                j = middle_index
            else:
                return True
        if matrix[target_index][i] == target:
            return True
        return False