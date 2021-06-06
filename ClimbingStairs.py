'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
class Solution:
    def climbStairs(self, n: int) -> int:  
        if n < 2:
            return 1
        '''step = [0 for _ in range (n)]
        step[0] = 1
        step[1] = 2
        for i in range(2, n):
            step[i] = step[i-1]+step[i-2]
        return step[-1]'''
        
        one = 1
        two = 1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
            
'''
Success
Details 
Runtime: 24 ms, faster than 93.41% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.1 MB, less than 89.70% of Python3 online submissions for Climbing Stairs.
'''