'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = []
        maxright = []
        
        water = 0
        def left(height):
            maxyet = 0
            for i in range(len(height)):
                if i==0:
                    maxleft.insert(0, 0)
                else:
                    maxleft.insert(i, max(maxyet, height[i-1]))
                    maxyet = max(maxyet, max(maxleft))
                    
            return maxleft
        
        
        def right(height):
            maxyet = 0

            for i in range(len(height),0, -1):
                if i==len(height):
                    maxright.insert(len(height),0)
                    print('here: ',maxright)
                else:
                    maxright.insert(i,max(maxyet, height[i]))
                    maxyet = max(maxyet,max(maxright))
            return maxright
    
    
        maxleft = left(height)
        maxright = right(height)
        maxright = sorted(maxright, reverse =True)
        print('final', maxright)
        minLR = []
        print(maxleft)
        print(maxright)
        for i in range(len(height)):
            minLR.append(min(maxleft[i],maxright[i]))
        print(minLR)            
        
        for i in range(len(height)):
            water += max(0,minLR[i] - height[i])
            
        return water