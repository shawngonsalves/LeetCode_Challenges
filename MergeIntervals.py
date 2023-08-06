# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastend = res[-1][1]
            if start <= lastend:
                res[-1][1] = max(end, lastend)
            else:
                res.append([start,end])
        return res

# Runtime 137 ms Beats 93.61%
# Memory 21.4 MB Beats 8.24%

