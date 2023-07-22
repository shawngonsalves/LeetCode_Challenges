# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        cache = set()

        def dfs(i,j, x):
            if x == len(word):
                return True
            if (i < 0 or j < 0 or 
                i >= ROWS or j >= COLS or
                (i,j) in cache or
                board[i][j] != word[x]):
                return False
            
            cache.add((i,j))
            
            res = (dfs(i+1, j, x+1) or
                  dfs(i-1, j, x+1) or
                  dfs(i, j+1, x+1) or
                  dfs(i, j-1, x+1))
            cache.remove((i,j))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False
    

# Runtime 7708 ms Beats 49.60%
# Memory 16.3 MB Beats 74.74%