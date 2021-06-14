'''
You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, 
p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

 

Example 1:

Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.
Example 2:

Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
Output: 1
Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
"abcd" is a subsequence of "abcddddd".
'''

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def isSubseq(s,subseq, removed):
            i1 = 0
            i2 = 0
            
            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1+=1
                    continue
                i1+=1
                i2+=1
            return i2 == len(subseq)
        
        res = 0
        l, r = 0, len(removable) - 1
        
        while l <= r:
            m = (l+r)//2
            removed  = set(removable[:m+1])
            if isSubseq(s, p, removed):
                res = max(res, m+1)
                l = m+1
            else:
                r = m-1
                
        return res

'''
Runtime: 4072 ms, faster than 45.45% of Python3 online submissions for Maximum Number of Removable Characters.
Memory Usage: 32.1 MB, less than 17.70% of Python3 online submissions for Maximum Number of Removable Characters.
'''