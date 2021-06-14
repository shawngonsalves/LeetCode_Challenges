'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
	        return 0
        if x > 0:
	        rev = str(x)
	        rev = rev[::-1]
	        if int(rev) > 2 ** 31:
		        return 0
	        return (int(rev))
        if x < 0:
	        x = x * -1
	        rev = str(x)
	        rev = rev[::-1]
	        if int(rev) > 2 ** 31:
		        return 0
	        return (int(rev) * -1)

'''
Runtime: 16 ms, faster than 99.97% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 43.19% of Python3 online submissions for Reverse Integer.
'''