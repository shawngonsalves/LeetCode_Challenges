'''
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res, left = set(), set()
        right = collections.Counter(s)
        
        
        for i in range(len(s)):
            right[s[i]]-=1
            if right[s[i]]==0:
                right.pop(s[i])
                
            for j in range(26):
                c = chr(ord('a')+j)
                if c in left and c in right:
                    res.add((s[i],c))
            left.add(s[i])
        print(res)    
        return len(res)

'''
Runtime: 6756 ms, faster than 25.00% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
Memory Usage: 15.5 MB, less than 25.00% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
'''