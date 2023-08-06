# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda i:i[0])
        intervals.sort()
        removals = 0
        prevstart, prevend = intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevend:
                removals +=1
                #remove interval with greater end val (prevend vs end)
                prevend = min(end, prevend)
            
            else:
                prevstart, prevend = start, end

        return removals
    
# Runtime 1200 ms Beats 96.24%
# Memory 55.2 MB Beats 80.76%