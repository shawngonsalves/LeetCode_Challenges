# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.



class Solution:
    def isPalindrome(self, s: str) -> bool:      
        
        # newS = ''
        # for char in s:
        #     if char.isalnum():
        #         newS += char.lower()


        # return newS == newS[::-1]

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.isalpha(s[l]):
                l += 1
            while r > l and not self.isalpha(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def isalpha(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))





        # s = s.lower()

        # s = s.strip()
        # print(s)
        # news = ""

        # l = []

        # for i in range(97, 123):
        #     l.append(chr(i))

        # for i in range(0, 10):
        #     l.append(str(i))
        # print(l)

        # for i in s:
        #     if i in l:
        #         news += i
        # print(news)           

        

        # if news == news[::-1]:
        #     return True
        # else:
        #     return False

# Runtime 72 ms Beats 28.30%
# Memory 17.2 MB Beats 53.16%