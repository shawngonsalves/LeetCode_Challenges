'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        
        
        
        
        
        for i in range(len(s)):
            l, r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)
                    
                l-=1
                r+=1
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)
                    
                l-=1
                r+=1
        
        
        
        return res

'''
Success
Details 
Runtime: 1344 ms, faster than 45.36% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.1 MB, less than 93.48% of Python3 online submissions for Longest Palindromic Substring.
'''

'''
Runtime482 ms Beats 60.76%
Memory 16.5 MB Beats 23.34%
'''