'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        merged_intervals = []
        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
           
            if start <= prev_end:
                prev_end = max(prev_end, end) 
            else:
                merged_intervals.append([prev_start, prev_end]) 
                prev_start, prev_end = start, end 

        
        merged_intervals.append([prev_start, prev_end])

        return merged_intervals

'''
Runtime 121 ms Beats 71.10% of users with Python3
Memory 21.29 MB Beats 28.88% of users with Python3
'''

