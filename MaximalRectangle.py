# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        temp = [0] * len(matrix[0])
        ROWS, COLS = len(matrix), len(matrix[0])
        maxArea = 0
        area = 0

        def maxHistogram(heights):
            stack = [-1]
            max_area = 0
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    current_height = heights[stack.pop()]
                    current_width = i - stack[-1] - 1
                    max_area = max(max_area, current_height * current_width)
                stack.append(i)
        
            while stack[-1] != -1:
                current_height = heights[stack.pop()]
                current_width = len(heights) - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            return max_area

        for i in range(ROWS):
            for j in range(len(temp)):
                if matrix[i][j] == "0":
                    temp[j] = 0
                else:
                    temp[j] += 1
            print(temp)
            area = max(area, maxHistogram(temp))
        return area
    
# Runtime 244 ms Beats 93.81%
# Memory 17.6 MB Beats 72.80%