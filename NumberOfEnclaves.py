class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        #totalland- borderland = res


        
        def dfs(r, c):
            if (r == ROWS or r < 0 or c<0 or c == COLS or (r,c) in visit or grid[r][c] ==0):
                return 0
            visit.add((r,c))
            res = 1
            dir = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in dir:
               res += dfs(r+dr, c+dc)
            return res


        land, border = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                land+=grid[r][c]
                if grid[r][c] == 1 and (r,c) not in visit and(c in [0,COLS-1] or r in [0,ROWS-1]):
                    border += dfs(r,c)
        return land - border
