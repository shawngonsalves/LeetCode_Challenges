class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] ==0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            peri = dfs(r, c+1)
            peri += dfs(r, c-1)
            peri += dfs(r-1,c)
            peri+= dfs(r+1,c)
            return peri


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)


