class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            t, r, c = heapq.heappop(minH)
            
            if (r ==N-1 and c == N-1):
                return t
            for dr, dc in directions:
                R , C = r + dr, c + dc
                if (R< 0 or C < 0 or R == N or C==N or (R, C) in visit):
                    continue
                visit.add((R,C))
                heapq.heappush(minH, [max(t, grid[R][C]), R, C])


