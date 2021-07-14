'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [intervals[i][0] for i in range(len(intervals))]
        start.sort()
        
        end = [intervals[i][1] for i in range(len(intervals))]
        end.sort()
        
        s,e = 0,0
        res, count =0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(res,count)
            
        return res

'''
Runtime: 80 ms, faster than 55.57% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 17.5 MB, less than 64.99% of Python3 online submissions for Meeting Rooms II.
'''