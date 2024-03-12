'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0
        open_bracket = 0
        
        ans = 0
        for char in s:
            if char == "(":
                open_bracket += 1
            else: 
                open_bracket -= 1
            if open_bracket < 0:
                open_bracket = 0
                ans += 1
        return ans + open_bracket
            


'''
Runtime 29 ms Beats 90.45% of users with Python3
Memory 16.56 MB Beats 48.59% of users with Python3
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s= s.replace("()","")
        return len(s)

'''
Runtime 34 ms Beats 67.68% of users with Python3
Memory 16.44 MB Beats 91.61% of users with Python3
'''