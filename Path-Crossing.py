'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        Hashset = set()
        x, y = 0, 0
        dir = {
                "N": [0,1],
                "S":[0, -1],
                "E":[1, 0], 
                "W":[-1, 0]
                }
        for c in path:
            Hashset.add((x, y))
            dx, dy = dir[c]
            x, y = x + dx, y + dy
            if (x,y) in Hashset:
                return True
        return False

'''
Runtime 34 ms Beats 72.49%
Memory 17.4 MB Beats 72.27%
'''