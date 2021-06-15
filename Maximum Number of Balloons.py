'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

 
Example 1:

Input: text = "nlaebolko"
Output: 1


Example 2:

Input: text = "loonbalxballpoon"
Output: 2
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for item in text:
            if item in ('b','a','l','l','o','o','n'):
                d[item] += 1
        if len(d) < 5 or d['l'] == 1 or d['o'] == 1:
            return 0
        
        print(d)
        d['l'] = d['l'] // 2
        d['o'] = d['o'] // 2
        return min(d.values())

'''
Runtime: 36 ms, faster than 54.39% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 14 MB, less than 98.87% of Python3 online submissions for Maximum Number of Balloons.
'''
