'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        
        def rec(r,c, M):
            if r < 0 or c < 0 or r>= m or c>=n:
                return 1
            if M == 0:
                return 0
            if (r,c,M) in memo: return memo[(r,c,M)]
            ans = 0
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                ans += rec(r+x, c+y, M-1)
                
            memo[(r,c,M)] = ans
            return ans
        
        return rec(startRow,startColumn, maxMove)%(10**9+7)
            