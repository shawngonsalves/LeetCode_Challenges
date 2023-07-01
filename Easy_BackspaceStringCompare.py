'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:
            if i =="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        
        for i in t:
            if i =='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        
        return True if stack1 == stack2 else False 
    

'''
Runtime 38 ms Beats 94.84%
Memory 16.4 MB Beats 6.41%
'''