class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        start_r, start_c, end_r, end_c = 0,0,0,0
        empty = 0
        visited =set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 2:
                    end_r, end_c = r,c
                elif grid[r][c] ==0:
                    empty += 1

        self.output = 0

        def dfs(r, c, visited, walk):
            if r ==end_r and c == end_c:
                if walk == empty +1:
                    self.output += 1
                return
            if 0<=r<ROWS and 0<=c<COLS and grid[r][c] != -1 and (r,c) not in visited:
                visited.add((r,c))
                for i,j in [(1,0), (0,1), (-1,0), (0,-1)]:
                    dfs(r+i, c+j, visited, walk+1)
                visited.remove((r,c))
        dfs(start_r,start_c, visited, 0)
        return self.output
            
