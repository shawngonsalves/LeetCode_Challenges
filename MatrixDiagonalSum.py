class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        res = 0
        n = len(mat)

        for i in range(n):
            res += mat[i][i]
            res += mat[i][n-1-i]
        
        return res - (mat[n//2][n//2] if n % 2 else 0)
