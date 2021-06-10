'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        path = set()
        
        def dfs(r, c, i):
            
            if i ==len(word):
                return True
            if (r < 0 or c < 0 or
                r>= ROWS or c >= COLS or
                ((r,c)) in path or word[i] != board[r][c]):
                return False
            path.add((r,c))
            
            
            res =  (dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
            ''' dfs recursive function main part of this backtracking problem '''
        
            ''' O(n*m* 4^n)'''
        
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0) : return True
        return False

