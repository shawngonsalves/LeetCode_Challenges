'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
 
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3**19 % n == 0)

'''
Runtime 54 ms Beats 91.18% of users with Python3
Memory 16.63 MB Beats 37.75% of users with Python3
'''