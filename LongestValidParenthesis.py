'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx

        # l, r = 0, 0
        # mx = 0

        # for p in s:
        #     if p == "(":
        #         l +=1
        #     else:
        #         r +=1
        #     if l == r:
        #         mx = max(mx, r**2)
        #     elif r > l:
        #         l, r = 0, 0
        # l, r = 0, 0
        # for p in reversed(s):
        #     if p == ")":
        #         r += 1
        #     else:
        #         l += 1
        #     if l == r:
        #         mx = max(mx, r**2)
        #     elif l > r:
        #         l, r = 0, 0
        # return mx

'''
Runtime 54 ms Beats 25.8%
Memory 16.9 MB Beats 46.79%
'''