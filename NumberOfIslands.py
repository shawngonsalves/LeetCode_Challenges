# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        res = 0
        def backtrack(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in visit:
                return 

            visit.add((r,c))


        

            backtrack(r+1, c)
            backtrack(r-1, c)
            backtrack(r, c+1)
            backtrack(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    res += 1
                    backtrack(r,c)
        return res
    
# Runtime 334 ms Beats 65.55%
# Memory 27.7 MB Beats 11.48%