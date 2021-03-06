'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        maxF = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r-l +1) - maxF > k:
                count[s[l]]-=1
                l+=1
                
            res = max(res, r-l+1)
        return res





'''
Success
Details 
Runtime: 104 ms, faster than 80.15% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.4 MB, less than 23.64% of Python3 online submissions for Longest Repeating Character Replacement.
Next challenges:
'''