'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for char in range(len(s)):
            if count[s[char]] == 1:
                return char
            
        return -1
'''
Runtime 92 ms Beats 63.39% of users with Python3
Memory 16.85 MB Beats 59.25% of users with Python3
'''