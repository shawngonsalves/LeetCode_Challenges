class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def DFS(i,j):
            if j >= len(t):
                return 1
            if i>= len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i]== t[j]:
                cache[(i,j)] = DFS(i+1,j+1)+ DFS(i+1,j)
            else:
                cache[(i,j)] = DFS(i+1,j)
                
            return cache[(i,j)]
        return DFS(0,0)