'''

Code
Testcase
Testcase
Test Result
939. Minimum Area Rectangle
Medium
Topics
Companies
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
'''

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float("inf")

        seen = set()

        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1 == x2) or (y1 == y2):
                    continue
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x2- x1)*abs(y2-y1)
                    if area and area < res:
                        res = area         
            seen.add((x1, y1))
        return res if res < float("inf") else 0

'''
Runtime 613 ms Beats 85.58% of users with Python3
Memory 16.89 MB Beats 90.44% of users with Python3
'''