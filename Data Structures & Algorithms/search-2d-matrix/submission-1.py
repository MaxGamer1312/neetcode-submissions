class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lOutside = 0
        rOutside = len(matrix) - 1
        while lOutside <= rOutside:
            midOutside = lOutside + ((rOutside - lOutside) // 2)
            if matrix[midOutside][0] > target:
                rOutside = midOutside - 1
            elif matrix[midOutside][len(matrix[midOutside]) - 1] < target:
                lOutside = midOutside + 1
            else:
                lInside = 0
                rInside = len(matrix[midOutside]) - 1
                while lInside <= rInside:
                    midInside = lInside + ((rInside - lInside) // 2) 
                    if matrix[midOutside][midInside] < target:
                        lInside = midInside + 1
                    elif matrix[midOutside][midInside] > target:
                        rInside = midInside - 1
                    else:
                        return True
                return False
        return False