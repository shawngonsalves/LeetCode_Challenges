class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >=0:
            cur = matrix[row][col]
            if cur == target:
                return True
            elif target < cur:
                col -= 1
            elif target > cur:
                row+=1
        return False
