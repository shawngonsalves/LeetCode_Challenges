'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(" ")
        output = ''
        for word in split:
            for letter in range(len(word)-1, -1, -1):
                output += word[letter]
            
            output += " "
        
        return str(output[:-1])

'''
Runtime 59 ms Beats 21.83%
Memory 16.9 MB Beats 79.72%
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        s = list(s)
        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_l, temp_r = l, r - 1

                if r == len(s) - 1:
                    temp_r = r

                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]  
                    temp_l +=1
                    temp_r -=1
                l = r + 1
        return "".join(s)
    
'''
Runtime 88 ms Beats 7.48%
Memory 16.8 MB Beats 93.8%
'''