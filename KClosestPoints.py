'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points      
        points.sort(key = lambda x: sqrt((x[0]**2) + (x[1]**2)))
        return (points[:k])
        '''if len(points) == k:
            return points
        p = points
        a = []
        for i in points:
            d = ((0-(i[0]))**2)+ ((0-(i[1]))**2)
            a.append(d)    
        res = []
        m = a
        temp = a
        print(m)
        for count,value in enumerate(m):
            
            b = min(a)
            
            print('now b is ', b)
            print('now value is', value)
            if b == value:
                print('went here')
                
                res.append(points[count])
                print('res is', res)
                
                temp.remove(b)
                k-=1
                print('now k is',  k)
                if k==0:
                    return res'''
                
'''
Success
Details 
Runtime: 620 ms, faster than 95.03% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.7 MB, less than 75.77% of Python3 online submissions for K Closest Points to Origin.
'''