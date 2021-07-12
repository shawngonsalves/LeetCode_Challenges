'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_key = {}
        t_key = {}
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            
            s_letter = s[i]
            t_letter = t[i]
            
            if s_letter not in s_key: s_key[s_letter] = i
                
            if t_letter not in t_key: t_key[t_letter] = i
                
            if s_key[s_letter] != t_key[t_letter]: return False
            
        return True