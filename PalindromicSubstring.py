'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def countPalindrome(l,r,s):
            res = 0
            while l >= 0 and r < len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
            
        
        for i in range(len(s)):
            l,r = i, i
            res+= countPalindrome(l,r,s)
            res+=countPalindrome(i,i+1,s)
            
        return res
    
        
                

'''
Success
Details 
Runtime: 128 ms, faster than 77.59% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14.4 MB, less than 51.82% of Python3 online submissions for Palindromic Substrings.
'''

